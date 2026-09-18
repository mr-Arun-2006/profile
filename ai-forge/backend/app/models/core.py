from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class AgentDefinition:
    id: str
    name: str
    role: str
    capabilities: list[str]
    description: str
    enabled: bool = True


AGENT_REGISTRY: dict[str, AgentDefinition] = {
    "planner": AgentDefinition(
        id="planner",
        name="Planner Agent",
        role="planning",
        capabilities=["planning", "task_graph", "dependencies"],
        description="Breaks user requests into tasks, selects agents, and creates execution plans.",
    ),
    "coding": AgentDefinition(
        id="coding",
        name="Coding Agent",
        role="coding",
        capabilities=["python", "javascript", "typescript", "fastapi", "react", "sql"],
        description="Handles implementation, debugging, refactoring, and configuration updates.",
    ),
    "backend": AgentDefinition(
        id="backend",
        name="Backend Agent",
        role="backend",
        capabilities=["api", "fastapi", "auth", "database", "services"],
        description="Owns backend APIs, auth flows, services, and business logic.",
    ),
    "frontend": AgentDefinition(
        id="frontend",
        name="Frontend Agent",
        role="frontend",
        capabilities=["ui", "ux", "react", "css", "accessibility"],
        description="Improves frontend UX, responsiveness, accessibility, and component architecture.",
    ),
    "database": AgentDefinition(
        id="database",
        name="Database Agent",
        role="database",
        capabilities=["postgresql", "sql", "migrations", "queries"],
        description="Manages schema, migrations, optimization, and data correctness.",
    ),
    "vision": AgentDefinition(
        id="vision",
        name="Vision Agent",
        role="vision",
        capabilities=["vision", "screenshots", "ui_inspection", "comparison"],
        description="Handles UI inspection, diagrams, and image understanding tasks.",
    ),
    "image": AgentDefinition(
        id="image",
        name="Image Agent",
        role="image_generation",
        capabilities=["image_generation", "image_editing", "illustration"],
        description="Generates and edits visuals, background assets, and illustrations.",
    ),
    "ocr": AgentDefinition(
        id="ocr",
        name="OCR Agent",
        role="ocr",
        capabilities=["ocr", "scan", "pdf", "text_extraction"],
        description="Extracts and structures text from scans, screenshots, and PDFs.",
    ),
    "research": AgentDefinition(
        id="research",
        name="Research Agent",
        role="research",
        capabilities=["research", "comparison", "facts", "summaries"],
        description="Collects source material and provides evidence-backed research summaries.",
    ),
    "data": AgentDefinition(
        id="data",
        name="Data Agent",
        role="data_analysis",
        capabilities=["data_analysis", "pandas", "python", "sql", "visualization"],
        description="Performs exploratory analysis, statistics, and data-driven reporting.",
    ),
    "testing": AgentDefinition(
        id="testing",
        name="Testing Agent",
        role="testing",
        capabilities=["unit_tests", "integration_tests", "api_tests", "regression"],
        description="Runs and diagnoses tests across backend, frontend, and integration layers.",
    ),
    "security": AgentDefinition(
        id="security",
        name="Security Agent",
        role="security",
        capabilities=["auth", "authorization", "vulnerabilities", "hardening"],
        description="Reviews code for exposure risks, auth issues, and unsafe patterns.",
    ),
    "reviewer": AgentDefinition(
        id="reviewer",
        name="Reviewer Agent",
        role="review",
        capabilities=["architecture", "code_review", "security_review", "quality"],
        description="Reviews requirements, architecture, code quality, and final implementation.",
    ),
}


def list_agents() -> list[dict[str, Any]]:
    return [
        {
            "id": agent.id,
            "name": agent.name,
            "role": agent.role,
            "capabilities": agent.capabilities,
            "description": agent.description,
            "enabled": agent.enabled,
        }
        for agent in AGENT_REGISTRY.values()
    ]


def get_agent(agent_id: str) -> AgentDefinition | None:
    return AGENT_REGISTRY.get(agent_id)


__all__ = ["AgentDefinition", "AGENT_REGISTRY", "get_agent", "list_agents"]
