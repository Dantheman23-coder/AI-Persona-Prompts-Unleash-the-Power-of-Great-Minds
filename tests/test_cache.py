from personacraft.cache import Cache


def test_cache():
    c = Cache()
    c.set("k", "v")
    assert c.get("k") == "v"
