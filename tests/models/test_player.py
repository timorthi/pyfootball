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
        except Exception as e:
            print("Setting up Player object failed:")
            traceback.print_exc()
            self.skipTest(TestPlayerAfterInit)

    def tearDown(self):
        self.player = None

    def test_data_types(self):
        self.assertIsInstance(self.player.name, str)
        self.assertIsInstance(self.player.position, str)
        self.assertIsInstance(self.player.jersey_number, int)
        self.assertIsInstance(self.player.date_of_birth, date)
        self.assertIsInstance(self.player.nationality, str)
        self.assertIsInstance(self.player.contract_until, date)
        self.assertIsInstance(self.player.market_value, str)

if __name__ == '__main__':
    unittest.main()