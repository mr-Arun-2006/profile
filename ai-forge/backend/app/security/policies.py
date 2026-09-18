from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class RepoInfo:
    owner: str
    repo: str
    default_branch: str = "main"
    permissions: dict[str, bool] | None = None


class GitHubGateway:
    """Internal GitHub access layer that never passes tokens to the model."""

    def __init__(
        self,
        app_id: str = "",
        private_key_path: str = "",
        client_id: str = "",
        client_secret: str = "",
    ) -> None:
        self.app_id = app_id
        self.private_key_path = private_key_path
        self.client_id = client_id
        self.client_secret = client_secret

    def list_repositories(self) -> list[str]:
        return ["mr-Arun/project-a", "mr-Arun/project-b", "organization/project-c"]

    def get_repository(self, owner: str, repo: str) -> RepoInfo:
        return RepoInfo(
            owner=owner,
            repo=repo,
            default_branch="main",
            permissions={"read": True, "write": True, "pull_request": True},
        )

    def list_files(self, owner: str, repo: str, ref: str = "main") -> list[str]:
        return [
            "src/auth/login.py",
            "src/auth/session.py",
            "src/frontend/LoginPage.tsx",
            "tests/test_auth.py",
        ]

    def read_file(self, owner: str, repo: str, path: str, ref: str = "main") -> dict[str, Any]:
        return {"path": path, "ref": ref, "content": f"# Example content for {path}\n# This is a secured backend-only read.", "truncated": False}

    def search_code(self, owner: str, repo: str, query: str, ref: str = "main") -> list[str]:
        return [f"{query} match in {owner}/{repo}"]

    def create_branch(self, owner: str, repo: str, branch_name: str) -> dict[str, Any]:
        return {"owner": owner, "repo": repo, "branch": branch_name, "status": "created"}

    def get_diff(self, owner: str, repo: str, base: str, head: str) -> dict[str, Any]:
        return {
            "files_changed": 3,
            "additions": 124,
            "deletions": 37,
            "summary": "Authentication fix + login redesign",
        }

    def create_commit(self, owner: str, repo: str, branch: str, message: str) -> dict[str, Any]:
        return {"owner": owner, "repo": repo, "branch": branch, "commit_message": message, "status": "created"}

    def create_pull_request(self, owner: str, repo: str, title: str, body: str, branch: str) -> dict[str, Any]:
        return {
            "owner": owner,
            "repo": repo,
            "title": title,
            "body": body,
            "branch": branch,
            "status": "pending_approval",
        }

    def get_pull_request(self, owner: str, repo: str, pull_request_number: int) -> dict[str, Any]:
        return {"owner": owner, "repo": repo, "number": pull_request_number, "state": "open"}
