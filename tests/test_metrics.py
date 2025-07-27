from personacraft.metrics import Score


def test_score_total():
    s = Score(1, 2, 3)
    assert s.total() == 6
