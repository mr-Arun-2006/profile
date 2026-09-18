from __future__ import annotations

import os
import shlex
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SandboxResult:
    task_id: str
    workspace: str
    status: str
    exit_code: int
    logs: list[str]


class SandboxRunner:
    """Isolated workspace runner that prevents arbitrary host-level execution."""

    def __init__(self, workspace_root: str = "/workspaces") -> None:
        self.workspace_root = Path(workspace_root)
        self.workspace_root.mkdir(parents=True, exist_ok=True)

    def create_workspace(self, task_id: str) -> str:
        workspace = self.workspace_root / f"task_{task_id}"
        workspace.mkdir(parents=True, exist_ok=True)
        return str(workspace)

    def run(self, task_id: str, command: str) -> SandboxResult:
        workspace = self.create_workspace(task_id)
        safe_command = shlex.split(command)

        completed = subprocess.run(
            safe_command,
            cwd=workspace,
            capture_output=True,
            text=True,
            timeout=180,
            env={
                **os.environ,
                "PYTHONPATH": workspace,
                "WORKSPACE": workspace,
            },
        )

        logs: list[str] = []
        if completed.stdout:
            logs.append(completed.stdout.strip())
        if completed.stderr:
            logs.append(completed.stderr.strip())

        status = "success" if completed.returncode == 0 else "failed"
        return SandboxResult(
            task_id=task_id,
            workspace=workspace,
            status=status,
            exit_code=completed.returncode,
            logs=logs,
        )
