"""Application unit test."""

import click
from click.testing import CliRunner

from app.util import constants
from app import crud

__author__ = "Harry Hum"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Harry Hum"
__email__ = "hum00051@algonquinlive.com"
__status__ = "Development"

# Global cheese array for command execution
cheese_array = []


def test_load():
    @click.command()
    @click.option("--path", default=constants.READ_FILE, help="Specify the path of the cheese csv file.")
    @click.option("--amount", default=200, help="Amount of records to read.")
    def load(path, amount):
        global cheese_array
        cheese_array = crud.load_csv(path, amount)

    runner = CliRunner()
    result = runner.invoke(load)


if __name__ == '__main__':
    test_load()