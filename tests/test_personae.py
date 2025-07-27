from personacraft import personae


def test_personae_count():
    assert len(personae.__all__) == 6
