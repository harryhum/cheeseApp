"""Contains cheese csv utility classes used by the Cheese app.

Classes: CheeseCSVParser, CheeseCSVWriter
"""

from app import constants
from app.models import Cheese

__author__ = "Harry Hum"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Harry Hum"
__email__ = "hum00051@algonquinlive.com"
__status__ = "Development"


class CheeseCSVParser:
    def __init__(self, csv):
        self.csv = csv

    def get_cheeses(self, rows):
        """Reads the specified amount of rows from the csv file.

        :param rows: Amount of rows to be read
        :return: An array of Cheese objects
        """
        line_count = 0
        cheese_array = []

        for row in self.csv:
            if line_count == 0:
                line_count += 1
            elif line_count < rows:
                cheese_array.append(self.parse_cheese(constants.ENGLISH_COLUMN_INDEXES, row))
                line_count += 1
            else:
                break

        return cheese_array

    @staticmethod
    def parse_cheese(column_indexes, record):
        """Parses a record in csv format and returns a cheese object.

        :param column_indexes: List of column header indexes
        :param record: Row in the csv
        :return: A Cheese object
        """
        if record is None:
            print("Nothing to parse.")
            pass
        else:
            trimmed_record = []
            for index in column_indexes:
                trimmed_record.append(record[index])

            return Cheese.from_array(trimmed_record)