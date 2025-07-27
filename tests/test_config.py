from personacraft.config import Settings


def test_settings_defaults():
    s = Settings()
    assert s.model == "gpt-4"
