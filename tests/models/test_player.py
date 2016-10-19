import unittest
import traceback
from datetime import date

from tests import resources
from pyfootball.models.player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        try:
            Player(resources.PLAYER)
        except:
            self.fail()

    def test_init_bad_data(self):
        with self.assertRaises(KeyError):
            Player({"a": "dict", "that": "has", "bad": "data"})


class TestPlayerAfterInit(unittest.TestCase):
    def setUp(self):
        try:
            self.player = Player(resources.PLAYER)
        except Exception:
            print("Setting up Player object failed:")
            traceback.print_exc()
            self.skipTest(TestPlayerAfterInit)

    def tearDown(self):
        self.player = None

    def test_data_types(self):
        integers = ['jersey_number']
        dates = ['date_of_birth', 'contract_until']

        for attr, val in self.player.__dict__.items():
            if attr in integers:
                self.assertIsInstance(val, int)
            elif attr in dates:
                self.assertIsInstance(val, date)
            else:  # Strings
                self.assertIsInstance(val, str)

if __name__ == '__main__':
    unittest.main()
