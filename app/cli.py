"""A command line application which reads and parses records from the cheese CSV file and allows users to display,
create, edit or delete records.

Uses the Click package for receiving command line input.
"""

import os

import click
import click_repl
from prompt_toolkit.history import FileHistory

from app import constants
from app.crud import load_csv
from app.models import Cheese

__author__ = "Harry Hum"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Harry Hum"
__email__ = "hum00051@algonquinlive.com"
__status__ = "Development"

# Global cheese array for command execution
cheese_array = []


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    click.echo("Canadian Cheese directory program by " + constants.MY_NAME)
    click.echo("Type '--help' to show the commands or show command options.")
    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)


@cli.command()
# TODO: turn path option into argument in the final edition of the program
@click.option("--path", default=constants.FILE_PATH, help="Specify the path of the cheese csv file.")
@click.option("--amount", default=200, help="Amount of records to read.")
def load(path, amount):
    global cheese_array
    cheese_array = load_csv(path, amount)


@cli.command()
def display():
    if not cheese_array:
        click.echo("No records loaded.")
    for cheese in cheese_array:
        click.echo(str(cheese))


# @cli.command()
# @cli.argument("id", type=str)
# @cli.argument("name", type=str)
# # TODO: add options for all attributes
# def add(id, name):
#     cheese = Cheese()
#     cheese.id = id
#     cheese.name = name


@cli.command()
def edit():
    print("edit")


@cli.command()
def delete():
    print("delete")


@cli.command()
def repl():
    """Start an interactive session"""
    prompt_kwargs = {
        'history': FileHistory(os.path.expanduser('~/.repl_history'))
    }
    click_repl.repl(click.get_current_context(), prompt_kwargs=prompt_kwargs)


if __name__ == "__main__":
    cli(obj={})
