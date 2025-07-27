"""Utility helpers."""


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-")
