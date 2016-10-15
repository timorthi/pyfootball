#from project directory: python -m unittest discover tests/

import unittest
import requests

import pyfootball
import pyfootball.config as config


class TestFootball(unittest.TestCase):

    def test_constructor_invalid(self):
        with self.assertRaises(requests.exceptions.HTTPError):
            f = pyfootball.Football("some_bogus_key")

    def test_constructor(self):
        try:
            f = pyfootball.Football(config.api_key)
        except:
            self.fail()

    def test_get_team(self):
        pass

if __name__ == '__main__':
    unittest.main()
