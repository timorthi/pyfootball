PLAYER = {
      "name": "Paul Pogba",
      "position": "Central Midfield",
      "jerseyNumber": 6,
      "dateOfBirth": "1993-03-15",
      "nationality": "France",
      "contractUntil": "2021-06-30",
      "marketValue": "70,000,000 €"
    }

PLAYERS = {
  "_links": {
    "self": {
      "href": "http://api.football-data.org/v1/teams/5/players"
    },
    "team": {
      "href": "http://api.football-data.org/v1/teams/5"
    }
  },
  "count": 4,
  "players": [
    {
      "name": "Manuel Neuer",
      "position": "Keeper",
      "jerseyNumber": 1,
      "dateOfBirth": "1986-03-27",
      "nationality": "Germany",
      "contractUntil": "2021-06-30",
      "marketValue": "45,000,000 €"
    },
    {
      "name": "Sven Ulreich",
      "position": "Keeper",
      "jerseyNumber": 26,
      "dateOfBirth": "1988-08-03",
      "nationality": "Germany",
      "contractUntil": "2018-06-30",
      "marketValue": "2,500,000 €"
    },
    {
      "name": "Tom Starke",
      "position": "Keeper",
      "jerseyNumber": 22,
      "dateOfBirth": "1981-03-18",
      "nationality": "Germany",
      "contractUntil": "2017-06-30",
      "marketValue": "200,000 €"
    },
    {
      "name": "Jérôme Boateng",
      "position": "Centre Back",
      "jerseyNumber": 17,
      "dateOfBirth": "1988-09-03",
      "nationality": "Germany",
      "contractUntil": "2021-06-30",
      "marketValue": "45,000,000 €"
    }]
    }

COMPETITION = {
  "_links": {
    "self": {
      "href": "http://api.football-data.org/v1/competitions/430"
    },
    "teams": {
      "href": "http://api.football-data.org/v1/competitions/430/teams"
    },
    "fixtures": {
      "href": "http://api.football-data.org/v1/competitions/430/fixtures"
    },
    "leagueTable": {
      "href": "http://api.football-data.org/v1/competitions/430/leagueTable"
    }
  },
  "id": 430,
  "caption": "1. Bundesliga 2016/17",
  "league": "BL1",
  "year": "2016",
  "currentMatchday": 8,
  "numberOfMatchdays": 34,
  "numberOfTeams": 18,
  "numberOfGames": 306,
  "lastUpdated": "2016-10-19T07:00:05Z"
}

COMP_TEAMS = {
  "_links": {
    "self": {
      "href": "http://api.football-data.org/v1/competitions/430/teams"
    },
    "competition": {
      "href": "http://api.football-data.org/v1/competitions/430"
    }
  },
  "count": 18,
  "teams": [
    {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/teams/5"
        },
        "fixtures": {
          "href": "http://api.football-data.org/v1/teams/5/fixtures"
        },
        "players": {
          "href": "http://api.football-data.org/v1/teams/5/players"
        }
      },
      "name": "FC Bayern München",
      "code": "FCB",
      "shortName": "Bayern",
      "squadMarketValue": "582,225,000 €",
      "crestUrl": "http://upload.wikimedia.org/wikipedia/commons/c/c5/Logo_FC_Bayern_München.svg"
    },
    {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/teams/12"
        },
        "fixtures": {
          "href": "http://api.football-data.org/v1/teams/12/fixtures"
        },
        "players": {
          "href": "http://api.football-data.org/v1/teams/12/players"
        }
      },
      "name": "Werder Bremen",
      "code": "SVW",
      "shortName": "Bremen",
      "squadMarketValue": "67,750,000 €",
      "crestUrl": "http://upload.wikimedia.org/wikipedia/commons/b/be/SV-Werder-Bremen-Logo.svg"
    },
    {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/teams/16"
        },
        "fixtures": {
          "href": "http://api.football-data.org/v1/teams/16/fixtures"
        },
        "players": {
          "href": "http://api.football-data.org/v1/teams/16/players"
        }
      },
      "name": "FC Augsburg",
      "code": "FCA",
      "shortName": "Augsburg",
      "squadMarketValue": "61,200,000 €",
      "crestUrl": "http://upload.wikimedia.org/wikipedia/de/b/b5/Logo_FC_Augsburg.svg"
    }]
    }

TEAM = {
  "_links": {
    "self": {
      "href": "http://api.football-data.org/v1/teams/5"
    },
    "fixtures": {
      "href": "http://api.football-data.org/v1/teams/5/fixtures"
    },
    "players": {
      "href": "http://api.football-data.org/v1/teams/5/players"
    }
  },
  "name": "FC Bayern München",
  "code": "FCB",
  "shortName": "Bayern",
  "squadMarketValue": "582,225,000 €",
  "crestUrl": "http://upload.wikimedia.org/wikipedia/commons/c/c5/Logo_FC_Bayern_München.svg"
}

FIXTURE = {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/fixtures/152247"
        },
        "competition": {
          "href": "http://api.football-data.org/v1/competitions/430"
        },
        "homeTeam": {
          "href": "http://api.football-data.org/v1/teams/6"
        },
        "awayTeam": {
          "href": "http://api.football-data.org/v1/teams/5"
        }
      },
      "date": "2016-09-09T18:30:00Z",
      "status": "FINISHED",
      "matchday": 2,
      "homeTeamName": "FC Schalke 04",
      "awayTeamName": "FC Bayern München",
      "result": {
        "goalsHomeTeam": 0,
        "goalsAwayTeam": 2
      },
      "odds": None
    }

FIXTURE_WITH_HT_AND_ODDS = {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/fixtures/149855"
        },
        "competition": {
          "href": "http://api.football-data.org/v1/competitions/424"
        },
        "homeTeam": {
          "href": "http://api.football-data.org/v1/teams/773"
        },
        "awayTeam": {
          "href": "http://api.football-data.org/v1/teams/811"
        }
      },
      "date": "2016-06-10T19:00:00Z",
      "status": "FINISHED",
      "matchday": 1,
      "homeTeamName": "France",
      "awayTeamName": "Romania",
      "result": {
        "goalsHomeTeam": 2,
        "goalsAwayTeam": 1,
        "halfTime": {
          "goalsHomeTeam": 0,
          "goalsAwayTeam": 0
        }
      },
      "odds": {
        "homeWin": 56,
        "draw": 15,
        "awayWin": 1.03
      }
    }

FIXTURES = {
  "_links": {
    "self": {
      "href": "http://api.football-data.org/v1/teams/5/fixtures"
    },
    "team": {
      "href": "http://api.football-data.org/v1/teams/5"
    }
  },
  "count": 3,
  "fixtures": [
    {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/fixtures/153633"
        },
        "competition": {
          "href": "http://api.football-data.org/v1/competitions/432"
        },
        "homeTeam": {
          "href": "http://api.football-data.org/v1/teams/49"
        },
        "awayTeam": {
          "href": "http://api.football-data.org/v1/teams/5"
        }
      },
      "date": "2016-08-19T18:45:00Z",
      "status": "FINISHED",
      "matchday": 1,
      "homeTeamName": "FC Carl Zeiss Jena",
      "awayTeamName": "FC Bayern München",
      "result": {
        "goalsHomeTeam": 0,
        "goalsAwayTeam": 5
      },
      "odds": {
        "homeWin": 56,
        "draw": 15,
        "awayWin": 1.03
      }
    },
    {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/fixtures/152258"
        },
        "competition": {
          "href": "http://api.football-data.org/v1/competitions/430"
        },
        "homeTeam": {
          "href": "http://api.football-data.org/v1/teams/5"
        },
        "awayTeam": {
          "href": "http://api.football-data.org/v1/teams/12"
        }
      },
      "date": "2016-08-26T18:30:00Z",
      "status": "FINISHED",
      "matchday": 1,
      "homeTeamName": "FC Bayern München",
      "awayTeamName": "Werder Bremen",
      "result": {
        "goalsHomeTeam": 6,
        "goalsAwayTeam": 0
      },
      "odds": {
        "homeWin": 1.12,
        "draw": 8,
        "awayWin": 26
      }
    },
    {
      "_links": {
        "self": {
          "href": "http://api.football-data.org/v1/fixtures/152247"
        },
        "competition": {
          "href": "http://api.football-data.org/v1/competitions/430"
        },
        "homeTeam": {
          "href": "http://api.football-data.org/v1/teams/6"
        },
        "awayTeam": {
          "href": "http://api.football-data.org/v1/teams/5"
        }
      },
      "date": "2016-09-09T18:30:00Z",
      "status": "FINISHED",
      "matchday": 2,
      "homeTeamName": "FC Schalke 04",
      "awayTeamName": "FC Bayern München",
      "result": {
        "goalsHomeTeam": 0,
        "goalsAwayTeam": 2
      },
      "odds": {
        "homeWin": 12,
        "draw": 6,
        "awayWin": 1.3
      }
    }]
    }

LEAGUE_TABLE = {
  "_links": {
    "self": {
      "href": "http://api.football-data.org/v1/competitions/430/leagueTable/?matchday=7"
    },
    "competition": {
      "href": "http://api.football-data.org/v1/competitions/430"
    }
  },
  "leagueCaption": "1. Bundesliga 2016/17",
  "matchday": 7,
  "standing": [
    {
      "_links": {
        "team": {
          "href": "http://api.football-data.org/v1/teams/5"
        }
      },
      "position": 1,
      "teamName": "FC Bayern München",
      "crestURI": "http://upload.wikimedia.org/wikipedia/commons/c/c5/Logo_FC_Bayern_München.svg",
      "playedGames": 7,
      "points": 17,
      "goals": 18,
      "goalsAgainst": 4,
      "goalDifference": 14,
      "wins": 5,
      "draws": 2,
      "losses": 0,
      "home": {
        "goals": 13,
        "goalsAgainst": 2,
        "wins": 3,
        "draws": 1,
        "losses": 0
      },
      "away": {
        "goals": 5,
        "goalsAgainst": 2,
        "wins": 2,
        "draws": 1,
        "losses": 0
      }
    },
    {
      "_links": {
        "team": {
          "href": "http://api.football-data.org/v1/teams/1"
        }
      },
      "position": 2,
      "teamName": "1. FC Köln",
      "crestURI": "http://upload.wikimedia.org/wikipedia/de/1/16/1._FC_Köln.svg",
      "playedGames": 7,
      "points": 15,
      "goals": 12,
      "goalsAgainst": 4,
      "goalDifference": 8,
      "wins": 4,
      "draws": 3,
      "losses": 0,
      "home": {
        "goals": 8,
        "goalsAgainst": 2,
        "wins": 3,
        "draws": 1,
        "losses": 0
      },
      "away": {
        "goals": 4,
        "goalsAgainst": 2,
        "wins": 1,
        "draws": 2,
        "losses": 0
      }
    },
    {
      "_links": {
        "team": {
          "href": "http://api.football-data.org/v1/teams/721"
        }
      },
      "position": 3,
      "teamName": "Red Bull Leipzig",
      "crestURI": "http://upload.wikimedia.org/wikipedia/de/d/d4/RB_Leipzig_2010_logo.svg",
      "playedGames": 7,
      "points": 15,
      "goals": 12,
      "goalsAgainst": 5,
      "goalDifference": 7,
      "wins": 4,
      "draws": 3,
      "losses": 0,
      "home": {
        "goals": 4,
        "goalsAgainst": 2,
        "wins": 2,
        "draws": 1,
        "losses": 0
      },
      "away": {
        "goals": 8,
        "goalsAgainst": 3,
        "wins": 2,
        "draws": 2,
        "losses": 0
      }
    }]
    }