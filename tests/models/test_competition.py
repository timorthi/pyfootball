import traceback
import unittest
from unittest.mock import Mock, patch
from datetime import datetime

from tests import resources
from pyfootball.models.competition import Competition
from pyfootball.models.team import Team
from pyfootball.models.fixture import Fixture
from pyfootball.models.leaguetable import LeagueTable


class TestCompetition(unittest.TestCase):
    def test_init(self):
        try:
            Competition(resources.COMPETITION)
        except:
            self.fail()

    def test_init_bad_data(self):
        with self.assertRaises(KeyError):
            Competition({"a": "dict", "that": "has", "bad": "data"})


class TestCompetitionAfterInit(unittest.TestCase):
    def setUp(self):
        try:
            self.comp = Competition(resources.COMPETITION)
        except Exception:
            print("Setting up Competition object failed:")
            traceback.print_exc()
            self.skipTest(TestCompetitionAfterInit)

    def tearDown(self):
        self.comp = None

    def test_data_types(self):
        strings = ['_teams_ep', '_fixtures_ep', '_league_table_ep',
                   'name', 'code']
        datetimes = ['last_updated']

        for attr, val in self.comp.__dict__.items():
            if attr in strings:
                self.assertIsInstance(val, str)
            elif attr in datetimes:
                self.assertIsInstance(val, datetime)
            else:  # Integers
                self.assertIsInstance(val, int)

    @patch('pyfootball.models.competition.requests.get')
    def test_get_fixtures(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = resources.FIXTURES

        fixtures = self.comp.get_fixtures()
        self.assertIsInstance(fixtures, list)
        for fixture in fixtures:
            self.assertIsInstance(fixture, Fixture)

    @patch('pyfootball.models.competition.requests.get')
    def test_get_teams(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = resources.COMP_TEAMS

        teams = self.comp.get_teams()
        self.assertIsInstance(teams, list)
        for team in teams:
            self.assertIsInstance(team, Team)

    @patch('pyfootball.models.competition.requests.get')
    def test_get_league_table(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = resources.LEAGUE_TABLE

        table = self.comp.get_league_table()
        self.assertIsInstance(table, LeagueTable)
