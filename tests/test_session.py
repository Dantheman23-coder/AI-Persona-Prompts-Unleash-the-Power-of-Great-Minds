from personacraft.session import new_session


def test_new_session():
    s = new_session("test")
    assert s.persona == "test"
