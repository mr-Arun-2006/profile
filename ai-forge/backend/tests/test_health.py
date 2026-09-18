from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.agents.registry import list_agents
from app.providers.registry import get_provider, list_providers
from app.orchestrator.planner import create_default_plan
from app.orchestrator.runtime import task_store


class TaskCreateRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    prompt: str = Field(..., min_length=10)
    mode: str = "assisted"


class ModelCreateRequest(BaseModel):
    provider: str
    model_id: str
    display_name: str
    description: str | None = None
    capabilities: list[str] = Field(default_factory=list)
    enabled: bool = True


app = FastAPI(title="AI Forge API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "service": "ai-forge-backend"}


@app.get("/api/providers")
def providers() -> list[dict[str, Any]]:
    return list_providers()


@app.post("/api/providers/{provider_id}/test")
async def test_provider(provider_id: str) -> dict[str, Any]:
    provider = get_provider(provider_id)
    health = await provider.test_connection()
    return {
        "provider": provider_id,
        "connected": health.connected,
        "status": health.status,
        "details": health.details,
    }


@app.get("/api/models")
def models() -> list[dict[str, Any]]:
    return [
        {
            "id": "nvidia-coding",
            "provider": "nvidia",
            "model_id": "meta/llama-3.1-70b-instruct",
            "display_name": "Llama 3.1 70B",
            "capabilities": ["coding", "reasoning"],
            "enabled": True,
            "priority": 100,
        },
        {
            "id": "openrouter-reasoning",
            "provider": "openrouter",
            "model_id": "openai/gpt-4o-mini",
            "display_name": "GPT-4o Mini",
            "capabilities": ["reasoning", "vision"],
            "enabled": True,
            "priority": 90,
        },
        {
            "id": "local-nim-coding",
            "provider": "local_nim",
            "model_id": "local-llm",
            "display_name": "Local LLM",
            "capabilities": ["coding"],
            "enabled": False,
            "priority": 50,
        },
    ]


@app.post("/api/models")
def create_model(payload: ModelCreateRequest) -> dict[str, Any]:
    return {
        "id": f"{payload.provider}-{payload.model_id}",
        "provider": payload.provider,
        "model_id": payload.model_id,
        "display_name": payload.display_name,
        "description": payload.description,
        "capabilities": payload.capabilities,
        "enabled": payload.enabled,
        "status": "registered",
    }


@app.put("/api/models/{model_id}")
def update_model(model_id: str, payload: ModelCreateRequest) -> dict[str, Any]:
    return {
        "id": model_id,
        "provider": payload.provider,
        "model_id": payload.model_id,
        "display_name": payload.display_name,
        "enabled": payload.enabled,
        "status": "updated",
    }


@app.get("/api/agents")
def agents() -> list[dict[str, Any]]:
    return list_agents()


@app.get("/api/tasks")
def tasks() -> list[dict[str, Any]]:
    records = task_store.list_tasks()
    return [
        {
            "id": task.id,
            "title": task.title,
            "status": task.status,
            "mode": task.mode,
            "plan": task.plan,
            "created_at": task.created_at.isoformat(),
        }
        for task in records
    ]


@app.post("/api/tasks")
def create_task(payload: TaskCreateRequest) -> dict[str, Any]:
    task = task_store.create_task(payload.title, payload.prompt, payload.mode)
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "mode": task.mode,
        "plan": task.plan,
    }


@app.get("/api/tasks/{task_id}")
def get_task(task_id: str) -> dict[str, Any]:
    task = task_store.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "mode": task.mode,
        "user_prompt": task.user_prompt,
        "plan": task.plan,
        "created_at": task.created_at.isoformat(),
    }


@app.post("/api/tasks/{task_id}/stop")
def stop_task(task_id: str) -> dict[str, Any]:
    task = task_store.stop_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task.id, "status": task.status, "message": "Task cancelled by user."}


@app.get("/api/tasks/{task_id}/events")
def get_task_events(task_id: str) -> list[dict[str, Any]]:
    events = task_store.get_events(task_id)
    return [
        {
            "task_id": event.task_id,
            "event": event.event,
            "timestamp": event.timestamp.isoformat(),
            "details": event.details,
        }
        for event in events
    ]


@app.get("/api/github/repositories")
def github_repositories() -> list[str]:
    return ["mr-Arun/project-a", "mr-Arun/project-b", "organization/project-c"]


@app.get("/api/prompts")
def prompts() -> list[dict[str, Any]]:
    return [
        {"id": "prompt_debugging", "category": "Debugging", "title": "Diagnose the issue"},
        {"id": "prompt_ui", "category": "UI Design", "title": "Design a login experience"},
        {"id": "prompt_security", "category": "Security", "title": "Review auth flow"},
    ]


@app.get("/api/usage")
def usage() -> dict[str, Any]:
    return {
        "requests_today": 132,
        "tokens_used": 184320,
        "estimated_cost": 12.84,
        "average_latency": 1140,
        "successful_tasks": 18,
        "failed_tasks": 2,
    }


@app.get("/api/audit")
def audit() -> list[dict[str, Any]]:
    return [
        {"timestamp": "2026-09-18T12:00:00Z", "actor": "Planner", "action": "Created execution plan"},
        {"timestamp": "2026-09-18T12:02:00Z", "actor": "GitHub Agent", "action": "READ_FILE src/auth/login.py"},
        {"timestamp": "2026-09-18T12:06:00Z", "actor": "User", "action": "APPROVED CREATE_PR"},
    ]


@app.get("/api/tasks/default-plan")
def default_plan() -> dict[str, Any]:
    return {"plan": create_default_plan()}
