import requests
import json

from . import endpoints
from . import globals
from .models.competition import Competition
from .models.team import Team


class Football(object):
    def __init__(self, api_key):
        """ Create a Football instance that serves as a driver for this
            library. Checks for validity of the API key by sending a test
            request. If this check fails, an HTTPError exception is raised.

            Arguments:
            api_key -- The user's football-data.org API key/token.
        """
        endpoint = endpoints.ALL_COMPETITIONS
        globals.headers = {'X-Auth-Token': api_key}
        r = requests.get(endpoint, headers=globals.headers)
        globals.update_prev_response(r, endpoint)
        r.raise_for_status()
        globals.api_key = api_key

    def get_prev_response(self):
        """ Returns information about the most recent response.

            Returns:
            prev_response -- A CaseInsensitiveDict containing response headers,
                             status code, and endpoint.
        """
        return globals.prev_response

    def get_competition(self, season=None):
        pass

    def get_team(self, team_id):
        """ Given an ID, returns a Team object for the team associated with
            the ID.

            Arguments:
            team_id -- The team ID. Can be a string or an integer.

            Returns:
            Team - The Team object.
        """
        endpoint = endpoints.TEAM.format(team_id)
        r = requests.get(endpoint, headers=globals.headers)
        globals.update_prev_response(r, endpoint)
        r.raise_for_status()
        return Team(data=r.json(), team_id=team_id)

    def search_teams(self, team_name):
        """ Given a team name, queries the database for matches and returns
            key-value pairs of their team IDs and team names.

            Arguments:
            team_name -- The partial or full team name.

            Returns:
            matches -- A dict with team ID as keys and team name as values.
            None -- If no matches are found for the given team_name.
        """
        name = team_name.replace(" ", "%20")
        endpoint = endpoints.TEAM.format('?name='+name)
        r = requests.get(endpoint, headers=globals.headers)
        globals.update_prev_response(r, endpoint)
        r.raise_for_status()

        data = r.json()
        if data['count'] is 0:
            return None
        else:
            matches = {}
            for team in data['teams']:
                matches[team['id']] = team['name']
            return matches
