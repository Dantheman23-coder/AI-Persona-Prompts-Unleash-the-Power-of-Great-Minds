from personacraft import logger


def test_logger_setup():
    logger.setup()
    assert logger.LOGGER.name == "personacraft"
