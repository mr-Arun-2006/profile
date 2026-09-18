from typing import Any


class TaskPlanner:
    def __init__(self, prompt: str) -> None:
        self.prompt = prompt

    def create_plan(self) -> list[str]:
        base_steps = [
            "Connect repository",
            "Analyze repository",
            "Detect authentication issue",
            "Fix backend",
            "Improve frontend",
            "Generate image",
            "Run tests",
            "Run security checks",
            "Review changes",
            "Request approval",
            "Create PR",
        ]
        return base_steps


def create_default_plan() -> list[str]:
    return TaskPlanner("Analyze my repository and fix the issue.").create_plan()
