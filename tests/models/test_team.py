import traceback
import unittest
from unittest.mock import Mock, patch

from tests import resources
from pyfootball.models.team import Team
from pyfootball.models.fixture import Fixture
from pyfootball.models.player import Player


class TestTeam(unittest.TestCase):
    def test_init(self):
        try:
            Team(resources.TEAM)
        except:
            self.fail()

    def test_init_bad_data(self):
        with self.assertRaises(KeyError):
            Team({"a": "dict", "that": "has", "bad": "data"})


class TestTeamAfterInit(unittest.TestCase):
    def setUp(self):
        try:
            self.team = Team(resources.TEAM)
        except Exception:
            print("Setting up Team object failed:")
            traceback.print_exc()
            self.skipTest(TestTeamAfterInit)

    def tearDown(self):
        self.team = None

    def test_data_types(self):
        integers = ['id']

        for attr, val in self.team.__dict__.items():
            if attr in integers:
                self.assertIsInstance(val, int)
            else:  # Strings
                self.assertIsInstance(val, str)

    @patch('pyfootball.models.team.requests.get')
    def test_get_fixtures(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = resources.FIXTURES

        fixtures = self.team.get_fixtures()
        self.assertIsInstance(fixtures, list)
        for fixture in fixtures:
            self.assertIsInstance(fixture, Fixture)

    @patch('pyfootball.models.team.requests.get')
    def test_get_players(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = resources.PLAYERS

        players = self.team.get_players()
        self.assertIsInstance(players, list)
        for player in players:
            self.assertIsInstance(player, Player)

if __name__ == '__main__':
    unittest.main()
