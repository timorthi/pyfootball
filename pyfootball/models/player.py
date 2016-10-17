import traceback
from datetime import datetime


class Player():
    def __init__(self, data):
        """Takes a dict converted from the JSON response by the API and wraps
        the player data within an object.

        :param data: The player data from the API's response.
        :type data: dict
        """
        try:
            self.name = data['name']
            self.position = data['position']
            self.jersey_number = data['jerseyNumber']
            self.date_of_birth = datetime.strptime(data['dateOfBirth'],
                                                   '%Y-%m-%d').date()
            self.nationality = data['nationality']
            self.contract_until = datetime.strptime(data['contractUntil'],
                                                    '%Y-%m-%d').date()
            self.market_value = data['marketValue']
        except KeyError:
            traceback.print_exc()
