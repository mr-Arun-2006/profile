from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class ModelRecord:
    id: str
    provider: str
    model_id: str
    display_name: str
    description: str | None = None
    capabilities: list[str] = field(default_factory=list)
    input_modalities: list[str] = field(default_factory=list)
    output_modalities: list[str] = field(default_factory=list)
    context_window: int | None = None
    supports_tools: bool = False
    supports_streaming: bool = False
    enabled: bool = True
    priority: int = 0
    cost_input: float | None = None
    cost_output: float | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class ProviderRecord:
    id: str
    name: str
    type: str
    status: str = "offline"
    base_url: str | None = None
    api_key_masked: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class PromptTemplate:
    id: str
    category: str
    title: str
    template: str = ""
    variables: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class TaskState:
    id: str
    title: str
    status: str = "CREATED"
    mode: str = "assisted"
    user_prompt: str = ""
    plan: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class AgentRun:
    id: str
    task_id: str
    agent_id: str
    model_id: str | None = None
    status: str = "QUEUED"
    input_summary: str = ""
    output_summary: str = ""
    latency_ms: int | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class ApprovalRecord:
    id: str
    task_id: str
    action: str
    requested_by: str
    approved: bool = False
    reason: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class ArtifactRecord:
    id: str
    type: str
    filename: str
    task_id: str | None = None
    model: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: dict[str, Any] = field(default_factory=dict)


__all__ = [
    "ModelRecord",
    "ProviderRecord",
    "PromptTemplate",
    "TaskState",
    "AgentRun",
    "ApprovalRecord",
    "ArtifactRecord",
]
