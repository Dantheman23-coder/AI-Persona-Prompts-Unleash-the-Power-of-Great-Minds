"""Package configuration."""

from dataclasses import dataclass


@dataclass
class Settings:
    model: str = "gpt-4"
    temperature: float = 0.7
