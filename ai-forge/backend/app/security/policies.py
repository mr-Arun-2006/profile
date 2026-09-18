from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RepoInfo:
    owner: str
    repo: str
    default_branch: str = "main"


class GitHubGateway:
    """Back-end only GitHub access layer with audit-friendly policy enforcement."""

    def __init__(self, app_id: str = "", private_key_path: str = "", client_id: str = "", client_secret: str = "") -> None:
        self.app_id = app_id
        self.private_key_path = private_key_path
        self.client_id = client_id
        self.client_secret = client_secret

    def list_repositories(self) -> list[str]:
        return ["mr-Arun/project-a", "mr-Arun/project-b", "organization/project-c"]

    def get_repository(self, owner: str, repo: str) -> RepoInfo:
        return RepoInfo(owner=owner, repo=repo, default_branch="main")

    def create_branch(self, owner: str, repo: str, branch_name: str) -> dict:
        return {"owner": owner, "repo": repo, "branch": branch_name, "status": "created"}

    def create_pull_request(self, owner: str, repo: str, title: str, body: str, branch: str) -> dict:
        return {"owner": owner, "repo": repo, "title": title, "branch": branch, "status": "pending_approval"}
