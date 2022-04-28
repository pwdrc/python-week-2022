from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornIPA", "--flavor=1", "--image=1", "--cost=1"]
    )
    assert result.exit_code == 0
    assert "Beer added to database" in result.stdout
