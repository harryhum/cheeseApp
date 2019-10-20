"""A command line application which reads and parses records from the cheese CSV file and allows users to display,
create, edit or delete records.

Uses the Click package for receiving command line input.
"""

import os

import click
import click_repl
from prompt_toolkit.history import FileHistory

from app import constants, crud
from app.cheese_csv_helper import CheeseCSVParser
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
# TODO: turn path option into argument in the final edition of the program, change default amount to 200
@click.option("--path", default=constants.READ_FILE, help="Specify the path of the cheese csv file.")
@click.option("--amount", default=10, help="Amount of records to read.")
def load(path, amount):
    """Load cheeses from a file."""
    global cheese_array
    cheese_array = crud.load_csv(path, amount)


@cli.command()
def display():
    """Display all loaded cheeses."""
    if not cheese_array:
        click.echo("No records loaded.")
    for cheese in cheese_array:
        click.echo(str(cheese))


@cli.command()
@click.argument("id")
@click.argument("name")
# TODO: add options for all attributes
def add(id, name):
    """Add a cheese to the records."""
    cheese = Cheese()
    cheese.id = id
    cheese.name = name
    cheese_array.append(cheese)


@cli.command()
def write():
    """Write records to new file."""
    crud.write_to_csv(constants.WRITE_FILE, cheese_array)

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
