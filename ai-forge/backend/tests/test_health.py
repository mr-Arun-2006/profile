from __future__ import annotations


class PolicyEngine:
    """Ensures least-privilege checks and approval gating for sensitive actions."""

    SENSITIVE_ACTIONS = {
        "create_pull_request",
        "merge",
        "delete_repository",
        "change_permissions",
        "modify_protected_branch",
        "expose_secret",
    }

    def authorize(self, actor: str, action: str, context: dict | None = None) -> bool:
        if action in self.SENSITIVE_ACTIONS:
            return False
        return actor in {"planner", "backend", "frontend", "reviewer", "testing", "security"}

    def explain(self, action: str) -> str:
        return f"Action '{action}' requires approval and audit logging."
