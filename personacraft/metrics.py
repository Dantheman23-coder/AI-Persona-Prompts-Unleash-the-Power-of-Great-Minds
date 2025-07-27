"""Simple scoring utilities."""

from dataclasses import dataclass


@dataclass
class Score:
    creativity: int
    persona_fidelity: int
    clarity: int

    def total(self) -> int:
        return self.creativity + self.persona_fidelity + self.clarity
