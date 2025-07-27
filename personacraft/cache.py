"""In-memory cache."""

from typing import Dict


class Cache:
    def __init__(self) -> None:
        self._data: Dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self._data.get(key)

    def set(self, key: str, value: str) -> None:
        self._data[key] = value
