import unittest
import traceback
from datetime import date

from tests import resources
from pyfootball.models.leaguetable import LeagueTable


class TestLeagueTable(unittest.TestCase):
    def test_init(self):
        try:
            LeagueTable(resources.LEAGUE_TABLE)
        except:
            self.fail()

    def test_init_bad_data(self):
        with self.assertRaises(KeyError):
            LeagueTable({"a": "dict", "that": "has", "bad": "data"})


class TestLeagueTableAfterInit(unittest.TestCase):
    def setUp(self):
        try:
            self.table = LeagueTable(resources.LEAGUE_TABLE)
        except Exception:
            print("Setting up LeagueTable object failed:")
            traceback.print_exc()
            self.skipTest(TestPlayerAfterInit)

    def tearDown(self):
        self.table = None

    def test_data_types(self):
        strings = ['_competition_ep', 'competition_name', 'team_name',
                   'crest_url']
        lists = ['standings']

        for attr, val in self.table.__dict__.items():
            if attr in strings:
                self.assertIsInstance(val, str)
            elif attr in lists:
                self.assertIsInstance(val, list)
            else:  # Integers
                self.assertIsInstance(val, int)

        dicts = ['home', 'away']
        for attr, val in self.table.standings[1].__dict__.items():
            """ Test only one Standing object. It can be assumed that every
            other Standing object in table.standings passes this test.
            """
            if attr in strings:
                self.assertIsInstance(val, str)
            elif attr in dicts:
                """The home and away dicts only contain keys which have integer
                values.
                """
                for key, value in val.items():
                    self.assertIsInstance(value, int)

            else:  # Integers
                self.assertIsInstance(val, int)

if __name__ == '__main__':
    unittest.main()
