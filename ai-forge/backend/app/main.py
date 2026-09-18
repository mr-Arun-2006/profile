from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class TaskRecord:
    id: str
    title: str
    status: str = "CREATED"
    mode: str = "assisted"
    user_prompt: str = ""
    plan: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class TaskEvent:
    task_id: str
    event: str
    timestamp: datetime
    details: dict[str, Any] | None = None


class InMemoryTaskStore:
    """In-memory task state and event stream for orchestration workflows."""

    def __init__(self) -> None:
        self.tasks: dict[str, TaskRecord] = {}
        self.events: dict[str, list[TaskEvent]] = {}

    def create_task(self, title: str, prompt: str, mode: str = "assisted") -> TaskRecord:
        from uuid import uuid4

        task_id = f"task_{uuid4().hex[:8]}"
        plan = [
            "Connect repository",
            "Analyze repository",
            "Detect authentication issue",
            "Fix backend",
            "Improve frontend",
            "Run tests",
            "Run security checks",
            "Review changes",
            "Request approval",
            "Create PR",
        ]
        task = TaskRecord(
            id=task_id,
            title=title,
            status="CREATED",
            mode=mode,
            user_prompt=prompt,
            plan=plan,
        )
        self.tasks[task_id] = task
        self.events[task_id] = []
        self.add_event(task_id, "TASK_CREATED", {"title": title, "mode": mode})
        self.add_event(task_id, "PLAN_CREATED", {"plan": plan})
        return task

    def add_event(self, task_id: str, event: str, details: dict[str, Any] | None = None) -> TaskEvent:
        task_event = TaskEvent(task_id=task_id, event=event, timestamp=datetime.now(timezone.utc), details=details)
        self.events.setdefault(task_id, []).append(task_event)
        return task_event

    def get_task(self, task_id: str) -> TaskRecord | None:
        return self.tasks.get(task_id)

    def list_tasks(self) -> list[TaskRecord]:
        return list(self.tasks.values())

    def get_events(self, task_id: str) -> list[TaskEvent]:
        return list(self.events.get(task_id, []))

    def set_task_status(self, task_id: str, status: str) -> TaskRecord | None:
        task = self.tasks.get(task_id)
        if task is None:
            return None
        task.status = status
        task.updated_at = datetime.now(timezone.utc)
        self.add_event(task_id, "STATUS_UPDATED", {"status": status})
        return task

    def stop_task(self, task_id: str) -> TaskRecord | None:
        return self.set_task_status(task_id, "CANCELLED")

    def add_step(self, task_id: str, step_name: str, status: str = "RUNNING", details: str | None = None) -> None:
        self.add_event(task_id, "STEP_CHANGED", {"step": step_name, "status": status, "details": details})


task_store = InMemoryTaskStore()
