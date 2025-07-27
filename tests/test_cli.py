from personacraft.cli import main


def test_cli(capsys):
    main(["persona", "--name", "Nikola Tesla", "--task", "innovate"])
    captured = capsys.readouterr()
    assert "Nikola Tesla" in captured.out
