import unittest
import traceback
from datetime import datetime

from tests import resources
from pyfootball.models.fixture import Fixture


class TestFixture(unittest.TestCase):
    def test_init(self):
        try:
            Fixture(resources.FIXTURE)
            Fixture(resources.FIXTURE_WITH_HT_AND_ODDS)
        except:
            self.fail()

    def test_init_bad_data(self):
        with self.assertRaises(KeyError):
            Fixture({"a": "dict", "that": "has", "bad": "data"})


class TestFixtureAfterInit(unittest.TestCase):
    def setUp(self):
        try:
            self.fixture = Fixture(resources.FIXTURE)
            self.fixture_full = Fixture(resources.FIXTURE_WITH_HT_AND_ODDS)
        except Exception:
            print("Setting up Fixture object(s) failed:")
            traceback.print_exc()
            self.skipTest(TestFixtureAfterInit)

    def tearDown(self):
        self.fixture = None
        self.fixture_full = None

    def test_data_types(self):
        integers = ['matchday', 'home_team_id', 'away_team_id',
                    'competition_id', 'home_team_goals, away_team_goals']
        dicts = ['result', 'odds']
        datetimes = ['date']

        for attr, val in self.fixture.__dict__.items():
            if attr in integers:
                self.assertIsInstance(val, int)
            elif attr in datetimes:
                self.assertIsInstance(val, datetime)
            elif attr in dicts:
                if attr is 'result':
                    for key, value in val.items():  # results dict
                        if key is 'half_time':
                            self.assertEqual(value, None)
                        else:
                            self.assertIsInstance(value, int)
                elif attr is 'odds':
                    self.assertEqual(val, None)
            else:  # Strings
                self.assertIsInstance(val, str)

        for attr, val in self.fixture_full.__dict__.items():
            if attr in integers:
                self.assertIsInstance(val, int)
            elif attr in datetimes:
                self.assertIsInstance(val, datetime)
            elif attr in dicts:
                if attr is 'result':
                    for key, value in val.items():  # results dict
                        if key is 'half_time':
                            for k, v in value.items():  # half_time dict
                                self.assertIsInstance(v, int)
                        else:
                            self.assertIsInstance(value, int)
                elif attr is 'odds':
                    for key, value in val.items():  # odds dict
                        self.assertIsInstance(value, float)
            else:  # Strings
                self.assertIsInstance(val, str)

if __name__ == '__main__':
    unittest.main()
