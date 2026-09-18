# AI Forge

AI Forge is a production-oriented orchestration platform for multi-model AI work across planning, coding, review, GitHub integration, testing, and artifact generation.

This repository contains an initial architecture and working project skeleton for the first implementation phases of the platform.

## Included

- Backend FastAPI server with provider and orchestration abstractions
- PostgreSQL-ready database layer and SQLAlchemy models
- Provider registry for NVIDIA API, OpenRouter, and Local NIM
- Security and GitHub gateway abstractions for least-privilege access
- Frontend React + Vite + TypeScript + Tailwind dashboard shell
- Docker Compose setup for local development
- Test scaffolding and environment template

## Structure

```text
ai-forge/
├── backend/
│   ├── app/
│   └── tests/
├── frontend/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── ARCHITECTURE.md
└── README.md
```

## Quick start

```bash
cd ai-forge
cp .env.example .env

docker compose up -d postgres
pip install -r backend/requirements.txt
cd backend && uvicorn app.main:app --reload
```

Then open the frontend:

```bash
cd frontend
npm install
npm run dev
```

## Notes

This implementation intentionally focuses on architecture, modular boundaries, and production-oriented scaffolding rather than a fake demo.
