import click
from flask.cli import AppGroup


mock_cli = AppGroup("mock")

@mock_cli.command("test")
# @click.option("--force", is_flag=True, help="Create after drop.")
@click.argument("name")
def test_cli(name):
    print(name)
