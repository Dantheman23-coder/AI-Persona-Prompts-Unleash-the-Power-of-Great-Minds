"""Simple logger."""

import logging

LOGGER = logging.getLogger("personacraft")


def setup(level: int = logging.INFO) -> None:
    logging.basicConfig(level=level)
