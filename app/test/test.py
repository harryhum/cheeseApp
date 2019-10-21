"""Application unit test."""

import unittest

from app import cli
from app.util import constants

__author__ = "Harry Hum"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Harry Hum"
__email__ = "hum00051@algonquinlive.com"
__status__ = "Development"


class TestCliApp(unittest.TestCase):

    def test_load_cheeses(self):
        cheese_array = cli.load(constants.TEST_READ_FILE, 1)
        cheese = cheese_array[0]

        self.assertEqual(cheese.id, "228")
        self.assertEqual(cheese.manufacturer_prov_code, "NB")
        self.assertEqual(cheese.manufacturer_type, "Farmstead")
        self.assertEqual(cheese.fat_content_percent, "24.2")
        self.assertEqual(cheese.moisture_percent, "47")
        self.assertEqual(cheese.flavour, "Sharp, lactic")
        self.assertEqual(cheese.characteristics, "Uncooked")
        self.assertEqual(cheese.ripening, "9 Months")
        self.assertEqual(cheese.category_type, "Firm Cheese")
        self.assertEqual(cheese.milk_type, "Ewe")
        self.assertEqual(cheese.rind_type, "Washed Rind")
        self.assertEqual(cheese.last_update_date, "2016-02-03")


if __name__ == '__main__':
    unittest.main()
