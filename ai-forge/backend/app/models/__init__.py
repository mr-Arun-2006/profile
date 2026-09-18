from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agents.registry import list_agents
from app.providers.registry import list_providers
from app.orchestrator.planner import create_default_plan

app = FastAPI(title="AI Forge API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "service": "ai-forge-backend"}


@app.get("/api/providers")
def providers() -> list[dict]:
    return list_providers()


@app.get("/api/models")
def models() -> list[dict]:
    return [
        {
            "id": "nvidia-coding",
            "provider": "nvidia",
            "model_id": "meta/llama-3.1-70b-instruct",
            "display_name": "Llama 3.1 70B",
            "capabilities": ["coding", "reasoning"],
            "enabled": True,
        },
        {
            "id": "openrouter-reasoning",
            "provider": "openrouter",
            "model_id": "openai/gpt-4o-mini",
            "display_name": "GPT-4o Mini",
            "capabilities": ["reasoning", "vision"],
            "enabled": True,
        },
    ]


@app.get("/api/agents")
def agents() -> list[dict]:
    return list_agents()


@app.get("/api/tasks")
def tasks() -> list[dict]:
    return [{"id": "task_demo_01", "status": "PLANNING", "title": "Analyze repository and fix auth bug"}]


@app.post("/api/tasks")
def create_task(payload: dict) -> dict:
    return {"id": "task_demo_01", "status": "CREATED", "title": payload.get("title", "New task"), "plan": create_default_plan()}


@app.get("/api/tasks/{task_id}")
def get_task(task_id: str) -> dict:
    return {"id": task_id, "status": "RUNNING", "title": "Repository analysis", "plan": create_default_plan()}


@app.get("/api/tasks/{task_id}/events")
def get_task_events(task_id: str) -> list[dict]:
    return [
        {"event": "TASK_CREATED", "task_id": task_id, "timestamp": "2026-09-18T12:00:00Z"},
        {"event": "PLAN_CREATED", "task_id": task_id, "timestamp": "2026-09-18T12:00:15Z"},
    ]


@app.get("/api/github/repositories")
def github_repositories() -> list[str]:
    return ["mr-Arun/project-a", "mr-Arun/project-b", "organization/project-c"]


@app.get("/api/prompts")
def prompts() -> list[dict]:
    return [{"id": "prompt_debugging", "category": "Debugging", "title": "Diagnose the issue"}]


@app.get("/api/usage")
def usage() -> dict:
    return {
        "requests_today": 132,
        "tokens_used": 184320,
        "estimated_cost": 12.84,
        "average_latency": 1140,
        "successful_tasks": 18,
        "failed_tasks": 2,
    }


@app.get("/api/audit")
def audit() -> list[dict]:
    return [
        {"timestamp": "2026-09-18T12:00:00Z", "actor": "Planner", "action": "Created execution plan"},
        {"timestamp": "2026-09-18T12:02:00Z", "actor": "GitHub Agent", "action": "READ_FILE src/auth/login.py"},
    ]
