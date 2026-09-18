AGENT_REGISTRY = {
    "orchestrator": {
        "name": "Orchestrator",
        "category": "coordination",
        "description": "Coordinates planning, execution, approvals, and delivery.",
    },
    "planner": {
        "name": "Planner",
        "category": "planning",
        "description": "Creates task graphs, dependencies, and execution sequencing.",
    },
    "backend": {
        "name": "Backend Agent",
        "category": "coding",
        "description": "Handles APIs, auth, business logic, and backend fixes.",
    },
    "frontend": {
        "name": "Frontend Agent",
        "category": "ui",
        "description": "Handles UX, responsive layouts, and login redesigns.",
    },
    "image": {
        "name": "Image Agent",
        "category": "visual",
        "description": "Generates UI assets, backgrounds, and illustrations.",
    },
    "testing": {
        "name": "Testing Agent",
        "category": "quality",
        "description": "Runs unit, integration, and regression validation.",
    },
    "security": {
        "name": "Security Agent",
        "category": "security",
        "description": "Scan for vulnerable patterns and unsafe operations.",
    },
    "reviewer": {
        "name": "Reviewer",
        "category": "review",
        "description": "Reviews final quality, architecture, and change risk.",
    },
}


def list_agents() -> list[dict]:
    return [
        {"id": key, "name": value["name"], "category": value["category"], "description": value["description"]}
        for key, value in AGENT_REGISTRY.items()
    ]
