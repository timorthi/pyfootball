import traceback
import requests

from pyfootball import endpoints
from pyfootball import globals
from .player import Player


class Team(object):
    def __init__(self, data, team_id):
        """ Takes a dict converted from the JSON response by the API and wraps
            the team data with an object.

            Keyword arguments:
            data -- A python dict converted from JSON containing the team data.
            team_id -- The team ID.
        """
        try:
            self._fixtures_ep = data['_links']['fixtures']['href']
            self._players_ep = data['_links']['players']['href']
            self.name = data['name']
            self.code = data['code']
            self.short_name = data['shortName']
            self.market_value = data['squadMarketValue']
            self.crest_url = data['crestUrl']
            self.id = team_id
        except KeyError:
            traceback.print_exc()

    def get_fixtures(self):
        pass

    def get_players(self):
        """ Return a list of Player objects representing players on the current
            team.

            Returns:
            players_list -- List containing Player objects
        """
        r = requests.get(self._players_ep, headers=globals.headers)
        globals.update_prev_response(r, self._players_ep)
        r.raise_for_status()

        data = r.json()
        player_list = []
        for player in data['players']:
            player_list.append(Player(player))
        return player_list
