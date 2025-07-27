from personacraft.persona import Persona


def test_render():
    p = Persona(name="Test", prompt="Do it")
    assert "Test" in p.render("solve")
