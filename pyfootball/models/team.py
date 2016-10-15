import traceback
import requests

from pyfootball import globals
from .player import Player
from .fixture import Fixture


class Team(object):
    def __init__(self, data):
        """ Takes a dict converted from the JSON response by the API and wraps
            the team data with an object.

            Keyword arguments:
            data -- A python dict converted from JSON containing the team data.
        """
        try:
            self._fixtures_ep = data['_links']['fixtures']['href']
            self._players_ep = data['_links']['players']['href']
            self.id = data['_links']['self']['href'].split("/")[-1]
            self.name = data['name']
            self.code = data['code']
            self.short_name = data['shortName']
            self.market_value = data['squadMarketValue']
            self.crest_url = data['crestUrl']
        except KeyError:
            traceback.print_exc()

    def get_fixtures(self):
        """ Return a list of Fixture objects representing this season's
            fixtures for the current team.

            Returns:
            fixture_list -- List containing Fixture objects
        """
        r = requests.get(self._fixtures_ep, headers=globals.headers)
        globals.update_prev_response(r, self._fixtures_ep)
        r.raise_for_status()

        data = r.json()
        fixture_list = []
        for fixture in data['fixtures']:
            fixture_list.append(Fixture(fixture))
        return fixture_list

    def get_players(self):
        """ Return a list of Player objects representing players on the current
            team.

            Returns:
            player_list -- List containing Player objects
        """
        r = requests.get(self._players_ep, headers=globals.headers)
        globals.update_prev_response(r, self._players_ep)
        r.raise_for_status()

        data = r.json()
        player_list = []
        for player in data['players']:
            player_list.append(Player(player))
        return player_list
