from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SecurityDecision:
    allowed: bool
    reason: str
    requires_approval: bool = False


class PolicyEngine:
    """Least-privilege policy checks for sensitive operations."""

    SENSITIVE_ACTIONS = {
        "create_pull_request",
        "merge",
        "delete_repository",
        "change_permissions",
        "modify_protected_branch",
        "expose_secret",
        "delete_production_resources",
    }

    def authorize(self, actor: str, action: str, context: dict | None = None) -> SecurityDecision:
        if action in self.SENSITIVE_ACTIONS:
            if context and context.get("approved") is True:
                return SecurityDecision(True, "Sensitive action approved by user.", False)
            return SecurityDecision(False, "Sensitive action requires explicit approval and audit logging.", True)

        allowed_actors = {"orchestrator", "planner", "backend", "frontend", "testing", "security", "reviewer"}
        if actor not in allowed_actors:
            return SecurityDecision(False, "Actor is not authorized for this action.", False)

        return SecurityDecision(True, "Action is within least-privilege policy.", False)

    def explain(self, action: str) -> str:
        return f"Action '{action}' follows least-privilege access and may require approval."

    def requires_approval(self, action: str) -> bool:
        return action in self.SENSITIVE_ACTIONS
