"""Library for all of the business logic for the CLI application.
"""

import csv
import sys
import traceback
from app.cheese_csv_helper import CheeseCSVParser

__author__ = "Harry Hum"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Harry Hum"
__email__ = "hum00051@algonquinlive.com"
__status__ = "Development"


def load_csv(path, records_to_read):
    """Load a csv with the csv reader.

    :param path: Path of file to be read
    :param records_to_read: Amount of records to read
    :return: An array of cheese objects
    """
    try:
        with open(path, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print(path + " opened successfully.")
            cheese_csv_parser = CheeseCSVParser(csv_reader)
            cheeses = cheese_csv_parser.get_cheeses(records_to_read)
        return cheeses

    except FileNotFoundError:
        print("Cannot find file at the path: " + path)
        traceback.print_exc(file=sys.stdout)

    except IOError:
        print("Error opening file: " + path)
        traceback.print_exc(file=sys.stdout)

def create_new_record(record):
    pass

# def write_to_csv(csv):
#
# def display_records(records):
#
# def edit_record(record):
#
# def delete_record(id):