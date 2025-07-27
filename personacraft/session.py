"""Session management."""

from uuid import uuid4

from .models import SessionModel


def new_session(persona: str) -> SessionModel:
    return SessionModel(id=str(uuid4()), persona=persona)
