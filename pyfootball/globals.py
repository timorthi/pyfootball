api_key = ""
headers = {}
prev_response = {}

_base = 'http://api.football-data.org'
endpoints = {
    'fixture': _base + '/v1/fixtures/{}',
    'all_fixtures': _base + '/v1/fixtures/',
    'competition': _base + '/v1/competitions/{}',
    'all_competitions': _base + '/v1/competitions/',
    'comp_teams': _base + '/v1/competitions/{}/teams',
    'comp_fixtures': _base + '/v1/competitions/{}/fixtures',
    'team': _base + '/v1/teams/{}',
    'team_players': _base + '/v1/teams/{}/players',
    'team_fixtures': _base + '/v1/teams/{}/fixtures/',
    'league_table': _base + '/v1/competitions/{}/leagueTable'
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
