from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Persona:
    """Simple representation of a persona."""

    name: str
    prompt: str
    voice_prompt: str | None = None

    def render(self, task: str) -> str:
        """Render the persona prompt with a task."""
        return f"As {self.name}, {task}. {self.prompt}"
