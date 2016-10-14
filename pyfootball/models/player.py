import traceback


class Player():
    def __init__(self, data):
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
