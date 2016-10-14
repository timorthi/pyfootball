import traceback

class Team(object):
    def __init__(self, data, id):
        """ Takes a dict converted from the JSON response by the API and wraps
            the team data with an object.

            Keyword arguments:
            data -- A python dict converted from JSON containing the team data.
        """
        try:
            self._fixtures_ep = data['_links']['fixtures']['href']
            self._players_ep = data['_links']['players']['href']
            self.name = data['name']
            self.code = data['code']
            self.short_name = data['shortName']
            self.market_value = data['squadMarketValue']
            self.crest_url = data['crestUrl']
            self.id = id
        except KeyError:
            traceback.print_exc()

    def get_fixtures(self):
        pass

    def get_players(self):
        pass
