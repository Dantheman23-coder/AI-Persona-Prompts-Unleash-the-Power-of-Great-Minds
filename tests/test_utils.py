from personacraft.utils import slugify


def test_slugify():
    assert slugify("Hello World") == "hello-world"
