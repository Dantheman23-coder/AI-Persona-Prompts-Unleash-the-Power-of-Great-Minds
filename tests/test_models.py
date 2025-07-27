from personacraft.models import PersonaModel


def test_model():
    m = PersonaModel(name="t", prompt="p")
    assert m.name == "t"
