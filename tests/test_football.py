import requests
import unittest
from unittest.mock import Mock, patch

from tests import resources
from pyfootball.football import Football
from pyfootball.models.competition import Competition


class TestFootball(unittest.TestCase):
    @patch('pyfootball.football.requests.get')
    def test_constructor_invalid_kwarg(self, mock_get):
        with self.assertRaises(requests.exceptions.HTTPError):
            http_err = requests.exceptions.HTTPError()
            mock_response = mock_get.return_value
            mock_response.raise_for_status.side_effect = http_err
            Football(api_key="some_bogus_key")

    @patch('pyfootball.football.requests.get')
    def test_constructor_envvar(self, mock_get):
        try:
            mock_response = mock_get.return_value
            mock_response.raise_for_status.side_effect = None
            Football()  # Uses PYFOOTBALL_API_KEY envvar
        except:
            self.fail()


@unittest.skip("Tests yet to be written.")
class TestFootballAfterInit(unittest.TestCase):
    def test_get_prev_response(self):
        pass

    def test_get_competition(self):
        pass

if __name__ == '__main__':
    unittest.main()
