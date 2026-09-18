from __future__ import annotations


class TaskPlanner:
    def __init__(self, prompt: str) -> None:
        self.prompt = prompt

    def create_plan(self) -> list[str]:
        return [
            "Connect repository",
            "Analyze repository",
            "Detect authentication issue",
            "Fix backend",
            "Improve frontend",
            "Generate illustration",
            "Run tests",
            "Run security checks",
            "Review changes",
            "Request approval",
            "Create PR",
        ]


def create_default_plan() -> list[str]:
    return TaskPlanner("Analyze repository and fix authentication issue.").create_plan()
