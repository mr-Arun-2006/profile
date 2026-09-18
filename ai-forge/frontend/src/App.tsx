from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_agents() -> None:
    response = client.get("/api/agents")
    assert response.status_code == 200
    assert len(response.json()) >= 3


def test_create_task() -> None:
    payload = {
        "title": "Diagnose auth flow",
        "prompt": "Analyze the repository and fix the authentication issue.",
        "mode": "assisted",
    }
    response = client.post("/api/tasks", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["status"] == "CREATED"
    assert isinstance(data["plan"], list)
    assert len(data["plan"]) > 0
