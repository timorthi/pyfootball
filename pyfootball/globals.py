api_key = ""
headers = {}
prev_response = {}

_base_endpoint = 'http://api.football-data.org/v1/'
endpoints = {
    'fixture': _base_endpoint + 'fixtures/{}',
    'all_fixtures': _base_endpoint + 'fixtures/',
    'competition': _base_endpoint + 'competitions/{}',
    'all_competitions': _base_endpoint + 'competitions/',
    'comp_teams': _base_endpoint + 'competitions/{}/teams',
    'comp_fixtures': _base_endpoint + 'competitions/{}/fixtures',
    'team': _base_endpoint + 'teams/{}',
    'team_players': _base_endpoint + 'teams/{}/players',
    'team_fixtures': _base_endpoint + 'teams/{}/fixtures/',
    'league_table': _base_endpoint + 'competitions/{}/leagueTable'
}


def update_prev_response(r, endpoint):
    """ Sets the prev_response attribute to contain a dict that includes
        the response status code and headers of the most recent HTTP
        request.

        Arguments:
        r -- The response object (of the latest HTTP request).
        endpoint -- The endpoint used (in the latest HTTP request).
    """
    global prev_response
    prev_response = r.headers
    prev_response['Status-Code'] = r.status_code
    prev_response['Endpoint'] = endpoint
