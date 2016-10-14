import os
import sys
sys.path.append("../")

import unittest
import requests

import pyfootball
import pyfootball.config as config


class TestFootball(unittest.TestCase):
    """
    def test_constructor_invalid(self):
        with self.assertRaises(requests.exceptions.HTTPError):
            f = pyfootball.Football("some_bogus_key")
    """

    def test_constructor(self):
        f = pyfootball.Football(config.api_key)
        self.assertEqual(f.api_key, config.api_key)

if __name__ == '__main__':
    unittest.main()
