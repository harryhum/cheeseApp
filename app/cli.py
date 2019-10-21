"""A command line application which reads and writes records from the cheese CSV file and allows users to create, read,
 update and delete records.

Uses the Click library for receiving command line input.
"""

import os

import click
import click_repl
from prompt_toolkit.history import FileHistory

from app import crud
from app.util import constants
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
    """This method is called when the program starts and is invoked again after every command."""
    show_name()
    click.echo("Type '--help' to show the commands or show command options.")
    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)


@cli.command()
@click.option("--path", default=constants.READ_FILE, help="Specify the path of the cheese csv file.")
@click.option("--amount", default=200, help="Amount of records to read.")
def load(path, amount):
    """Load cheeses from a file.

    :param path: Path of file to be read
    :param amount: Amount of records to read
    """
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
@click.option("--manufacturer_name", help="Optional manufacturer_name attribute")
@click.option("--manufacturer_prov_code", help="Optional manufacturer_prov_code attribute")
@click.option("--manufacturer_type", help="Optional manufacturer_type attribute")
@click.option("--website", help="Optional website attribute")
@click.option("--fat_content_percent", help="Optional fat_content_percent attribute")
@click.option("--moisture_percent", help="Optional moisture_percent attribute")
@click.option("--particularities", help="Optional particularities attribute")
@click.option("--flavour", help="Optional flavour attribute")
@click.option("--characteristics", help="Optional characteristics attribute")
@click.option("--ripening", help="Optional ripening attribute")
@click.option("--organic", help="Optional organic attribute")
@click.option("--category_type", help="Optional category_type attribute")
@click.option("--milk_type", help="Optional milk_type attribute")
@click.option("--milk_treatment_type", help="Optional milk_treatment_type attribute")
@click.option("--rind_type", help="Optional rind_type attribute")
@click.option("--last_update_date", help="Optional last_update_date attribute")
def add(id, name, manufacturer_name="", manufacturer_prov_code="", manufacturer_type="",
        website="", fat_content_percent="", moisture_percent="", particularities="", flavour="",
        characteristics="", ripening="", organic="", category_type="", milk_type="", milk_treatment_type="",
        rind_type="", last_update_date=""):
    """Add a cheese to the records.

    Id and name must be provided.

    :param id: id attribute
    :param name: name attribute
    :param manufacturer_name: manufacturer_name attribute
    :param manufacturer_prov_code: manufacturer_prov_code attribute
    :param manufacturer_type: manufacturer_type attribute
    :param website: website attribute
    :param fat_content_percent: fat_content_percent attribute
    :param moisture_percent: moisture_percent attribute
    :param particularities: particularities attribute
    :param flavour: flavour attribute
    :param characteristics: characteristics attribute
    :param ripening: ripening attribute
    :param organic: organic attribute
    :param category_type: category_type attribute
    :param milk_type: milk_type attribute
    :param milk_treatment_type: milk_treatment_type attribute
    :param rind_type: rind_type attribute
    :param last_update_date: last_update_date attribute
    """
    cheese = Cheese.from_array([id, name, manufacturer_name, manufacturer_prov_code, manufacturer_type,
                                website, fat_content_percent, moisture_percent, particularities, flavour,
                                characteristics, ripening, organic, category_type, milk_type, milk_treatment_type,
                                rind_type, last_update_date])
    cheese_array.append(cheese)


@cli.command()
def write():
    """Write records to new file.
    """
    crud.write_to_csv(constants.WRITE_FILE, cheese_array)
    click.echo("Records saved to '" + constants.WRITE_FILE + "'")


@cli.command()
@click.argument("id")
@click.option("--name", help="Optional name attribute change")
@click.option("--manufacturer_name", help="Optional manufacturer_name attribute change")
@click.option("--manufacturer_prov_code", help="Optional manufacturer_prov_code attribute change")
@click.option("--manufacturer_type", help="Optional manufacturer_type attribute change")
@click.option("--website", help="Optional website attribute change")
@click.option("--fat_content_percent", help="Optional fat_content_percent attribute change")
@click.option("--moisture_percent", help="Optional moisture_percent attribute change")
@click.option("--particularities", help="Optional particularities attribute change")
@click.option("--flavour", help="Optional flavour attribute change")
@click.option("--characteristics", help="Optional characteristics attribute change")
@click.option("--ripening", help="Optional ripening attribute change")
@click.option("--organic", help="Optional organic attribute change")
@click.option("--category_type", help="Optional category_type attribute change")
@click.option("--milk_type", help="Optional milk_type attribute change")
@click.option("--milk_treatment_type", help="Optional milk_treatment_type attribute change")
@click.option("--rind_type", help="Optional rind_type attribute change")
@click.option("--last_update_date", help="Optional last_update_date attribute change")
def edit(id, name, manufacturer_name="", manufacturer_prov_code="", manufacturer_type="",
         website="", fat_content_percent="", moisture_percent="", particularities="", flavour="",
         characteristics="", ripening="", organic="", category_type="", milk_type="", milk_treatment_type="",
         rind_type="", last_update_date=""):
    """Edit a record.

    :param id: id attribute
    :param name: name attribute
    :param manufacturer_name: manufacturer_name attribute
    :param manufacturer_prov_code: manufacturer_prov_code attribute
    :param manufacturer_type: manufacturer_type attribute
    :param website: website attribute
    :param fat_content_percent: fat_content_percent attribute
    :param moisture_percent: moisture_percent attribute
    :param particularities: particularities attribute
    :param flavour: flavour attribute
    :param characteristics: characteristics attribute
    :param ripening: ripening attribute
    :param organic: organic attribute
    :param category_type: category_type attribute
    :param milk_type: milk_type attribute
    :param milk_treatment_type: milk_treatment_type attribute
    :param rind_type: rind_type attribute
    :param last_update_date: last_update_date attribute
    """
    found = False
    for cheese in cheese_array:
        if id == cheese.id:
            found = True
            click.echo("Editing the following record:")
            click.echo("\t" + str(cheese))

            if name:
                cheese.name = name
            if manufacturer_name:
                cheese.manufacturer_name = manufacturer_name
            if manufacturer_prov_code:
                cheese.manufacturer_prov_code = manufacturer_prov_code
            if manufacturer_type:
                cheese.manufacturer_type = manufacturer_type
            if website:
                cheese.website = website
            if fat_content_percent:
                cheese.fat_content_percent =fat_content_percent
            if moisture_percent:
                cheese.moisture_percent = moisture_percent
            if particularities:
                cheese.particularities = particularities
            if flavour:
                cheese.flavour = flavour
            if characteristics:
                cheese.characteristics = cheese
            if ripening:
                cheese.ripening = ripening
            if organic:
                cheese.organic = organic
            if category_type:
                cheese.category_type = category_type
            if milk_type:
                cheese.milk_type = milk_type
            if milk_treatment_type:
                cheese.milk_treatment_type =milk_treatment_type
            if rind_type:
                cheese.rind_type = rind_type
            if last_update_date:
                cheese.last_update_date = last_update_date

            click.echo("Modified record:")
            click.echo("\t" + str(cheese))

    if not found:
        click.echo("No records found with id: " + id)


@cli.command()
@click.argument("id")
def delete(id):
    """Delete cheese from records.

    :param id: id attribute
    """
    found = False
    for cheese in cheese_array:
        if id == cheese.id:
            found = True
            click.echo("Deleting the following record:")
            click.echo("\t" + str(cheese))

            cheese_array.remove(cheese)
            click.echo("Record deleted.")

    if not found:
        click.echo("No records found with id: " + id)


@cli.command()
def repl():
    """Start an interactive session"""
    prompt_kwargs = {
        'history': FileHistory(os.path.expanduser('~/.repl_history'))
    }
    click_repl.repl(click.get_current_context(), prompt_kwargs=prompt_kwargs)


def show_name():
    """Show author name."""
    click.echo("Canadian Cheese directory program by " + constants.MY_NAME)


if __name__ == "__main__":
    cli(obj={})
