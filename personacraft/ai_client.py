"""Mock AI client interface."""

from dataclasses import dataclass


@dataclass
class AIClient:
    name: str = "mock"

    def chat(self, message: str) -> str:
        return f"[AI {self.name}] {message}"
