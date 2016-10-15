import traceback
import requests

from pyfootball import globals
from .team import Team


class Competition():
    def __init__(self, data):
        """ Takes a dict converted from the JSON response by the API and wraps
            the competition data within an object.

            Keyword arguments:
            data -- A python dict converted from JSON containing the team data.
        """
        try:
            self._teams_ep = data['_links']['teams']['href']
            self._fixtures_ep = data['_links']['fixtures']['href']
            self._league_table_ep = data['_links']['leagueTable']['href']
            self.id = data['id']
            self.name = data['caption']
            self.code = data['league']
            self.year = data['year']
            self.current_matchday = data['currentMatchday']
            self.number_of_matchdays = data['numberOfMatchdays']
            self.number_of_teams = data['numberOfTeams']
            self.number_of_games = data['numberOfGames']
            self.last_updated = data['lastUpdated']
        except KeyError:
            traceback.print_exc()

    def get_fixtures(self):
        pass

    def get_teams(self):
        """ Return a list of Team objects representing the teams in this
            competition for the current season.

            Returns:
            team_list -- List containing Team objects
        """
        r = requests.get(self._teams_ep, headers=globals.headers)
        globals.update_prev_response(r, self._teams_ep)
        r.raise_for_status()

        data = r.json()
        team_list = []
        for tm in data['teams']:
            team_list.append(Team(tm))
        return team_list

    def get_league_table(self):
        pass
