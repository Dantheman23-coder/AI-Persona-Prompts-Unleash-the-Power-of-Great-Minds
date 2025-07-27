from personacraft.ai_client import AIClient


def test_chat():
    client = AIClient()
    assert "AI" in client.chat("hi")
