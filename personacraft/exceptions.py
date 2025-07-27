"""Package specific exceptions."""


class PersonaCraftError(Exception):
    """Base error for PersonaCraft."""


class PersonaNotFound(PersonaCraftError):
    """Raised when a persona is not found."""
