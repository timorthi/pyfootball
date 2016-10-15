import traceback


class Player():
    def __init__(self, data):
        """ Takes a dict converted from the JSON response by the API and wraps
            the player data within an object.

            Keyword arguments:
            data -- A python dict converted from JSON containing the player
                    data.
        """
        try:
            self.name = data['name']
            self.position = data['position']
            self.jersey_number = data['jerseyNumber']
            self.date_of_birth = data['dateOfBirth']
            self.nationality = data['nationality']
            self.contract_until = data['contractUntil']
            self.market_value = data['marketValue']
        except KeyError:
            traceback.print_exc()
