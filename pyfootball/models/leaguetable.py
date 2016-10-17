import traceback


class LeagueTable(object):
    def __init__(self, data):
        """Takes a dict converted from the JSON response by the API and wraps
        the league table data within an object.

        :param data: The league table data from the API's response.
        :type data: dict
        """
        try:
            self._competition_ep = data['_links']['competition']['href']
            self.competition_id = self._competition_ep.split('/')[-1]
            self.competition_name = data['leagueCaption']
            self.current_matchday = data['matchday']

            _standings_list = [None]
            for pos in data['standing']:
                _standings_list.append(self.Standing(pos))

            self.standings = _standings_list
        except KeyError:
            traceback.print_exc()

    class Standing(object):
        def __init__(self, data):
            """A private LeagueTable class that stores information about
            a given position in the table.
            """
            try:
                self.position = data['position']
                self.team_id = data['_links']['team']['href'].split('/')[-1]
                self.team_name = data['teamName']
                self.crest_url = data['crestURI']
                self.games_played = data['playedGames']
                self.points = data['points']
                self.goals = data['goals']
                self.goals_against = data['goalsAgainst']
                self.goal_difference = data['goalDifference']
                self.wins = data['wins']
                self.draws = data['draws']
                self.losses = data['losses']
                self.home = {
                    'goals': data['home']['goals'],
                    'goals_against': data['home']['goalsAgainst'],
                    'wins': data['home']['wins'],
                    'draws': data['home']['draws'],
                    'losses': data['home']['losses']
                }
                self.away = {
                    'goals': data['away']['goals'],
                    'goals_against': data['away']['goalsAgainst'],
                    'wins': data['away']['wins'],
                    'draws': data['away']['draws'],
                    'losses': data['away']['losses']
                }
            except KeyError:
                traceback.print_exc()
