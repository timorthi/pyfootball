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
        self._update_previous_response(r, endpoint)
        r.raise_for_status()
        globals.api_key = api_key

    def _update_previous_response(self, r, endpoint):
        """ Sets the prev_response attribute to contain a dict that includes
            the response status code and headers of the most recent HTTP
            request.

            Arguments:
            r -- The response object (of the latest HTTP request).
            endpoint -- The endpoint used (in the latest HTTP request).
        """
        self.prev_response = r.headers
        self.prev_response['Status-Code'] = r.status_code
        self.prev_response['Endpoint'] = endpoint

    def get_competition(self, season=None):
        pass

    def get_team(self, team_id):
        """ Given an ID, returns a Team object for the team associated with
            the ID.

            Arguments:
            team_id -- The team ID.

            Returns:
            Team - The Team object.
        """
        endpoint = endpoints.TEAM.format(team_id)
        r = requests.get(endpoint, headers=globals.headers)
        self._update_previous_response(r, endpoint)
        r.raise_for_status()
        return Team(data=r.json(), team_id=team_id)

    def search_teams(self, team_name):
        """ Given a team name, queries the database for matches and returns
            a list of the Team object(s) of the matches, if any.

            Arguments:
            team_name -- The partial or full team name.

            Returns:
            None - If there are no matches, returns nothing.
            Team[] - A list of Team objects corresponding to successful matches
        """
        name = team_name.replace(" ", "%20")
        endpoint = endpoints.TEAM.format('?name='+name)
        r = requests.get(endpoint, headers=globals.headers)
        self._update_previous_response(r, endpoint)
        r.raise_for_status()

        data = r.json()
        if data['count'] is 0:
            return None
        else:
            return data['teams']
