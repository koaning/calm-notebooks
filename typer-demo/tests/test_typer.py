from typer.testing import CliRunner

from demopkg.__main__ import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["hello-world", "Vincent"])
    assert result.exit_code == 0
    assert "Vincent" in result.stdout


def test_db_create1():
    # Note that we need to confirm here, hence the extra input!
    result = runner.invoke(app, ["db", "create-db"], input="foobar\nfoobar\n")
    assert result.exit_code == 0
    assert "foobar" in result.stdout


def test_db_create2():
    # Note that we need to confirm here, hence the extra input!
    result = runner.invoke(app, ["db", "create-db", "--table", "foobar"], input="foobar\n")
    assert result.exit_code == 0
    print(result.stdout)
    assert "foobar" in result.stdout
