from personacraft.exceptions import PersonaNotFound


def test_exception_str():
    e = PersonaNotFound("oops")
    assert str(e) == "oops"
