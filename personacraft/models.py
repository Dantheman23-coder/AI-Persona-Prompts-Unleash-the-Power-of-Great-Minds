"""Pydantic models for PersonaCraft."""

from pydantic import BaseModel


class PersonaModel(BaseModel):
    name: str
    prompt: str
    voice_prompt: str | None = None


class SessionModel(BaseModel):
    id: str
    persona: str
    score: int | None = None
