import requests

from . import endpoints
from .models.competition import Competition
from .models.team import Team


class Football(object):
    def __init__(self, api_key):
        """ Create a Football instance that serves as a driver for this
            API wrapper. Sends a test request to ensure validity of API key.
            If this check fails, an HTTPError exception is raised.

            Arguments:
            api_key -- The user's football-data.org API key/token.
        """
        endpoint = endpoints.ALL_COMPETITIONS
        headers = {'X-Auth-Token': api_key}
        r = requests.get(endpoint, headers=headers)
        r.raise_for_status()

        self.api_key = api_key

    def get_competition(self, season=None):
        pass

    def get_team(self, id):
        """ Returns a Team object for the team associated with the given ID.

            Arguments:
            id -- The team ID.
        """
        endpoint = endpoints.TEAM.format(id)
        headers = {'X-Auth-Token': self.api_key}
        r = requests.get(endpoint, headers=headers)
        r.raise_for_status()
        pass

    def search_teams(team_name):
        pass
