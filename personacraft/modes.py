"""Gameplay modes."""

from dataclasses import dataclass


@dataclass
class Mode:
    name: str
    description: str


MODES = {
    "sprint": Mode("sprint", "Rapid ideation"),
    "masterclass": Mode("masterclass", "Deep dive"),
    "coop": Mode("coop", "Collaborative"),
    "challenge": Mode("challenge", "Hard problems"),
    "tutorial": Mode("tutorial", "Learning"),
    "freeplay": Mode("freeplay", "Open exploration"),
}
