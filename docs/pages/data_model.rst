Data Model
=============
The data model was designed to keep to the original data's structure as closely as possible. There were mostly minor changes as a result of following the `PEP8 guidelines <https://www.python.org/dev/peps/pep-0008/>`_ such as turning variable names from using ``camelCase`` to ``under_scores``.

Each `football-data.org resource <http://api.football-data.org/docs/v1/index.html#_resources>`_ is mapped into an object. Each value in a JSON resource is mapped to an attribute of the object. You can access these values using the syntax ``Object.attribute``. For example:
::

    >>> import pyfootball
    >>> f = pyfootball.Football('your_api_key')
    >>> my_team = f.get_team(5)
    >>> my_team.name
    FC Bayern München

Competition
------------

.. list-table::
    :widths: 40 40 100
    :header-rows: 1

    * - Attribute
      - Type
      - Description

    * - id
      - integer
      - The ID of the competition.

    * - name
      - string
      - The name of the competition.

    * - code
      - string
      - The `League Code <http://api.football-data.org/docs/v1/index.html#league_codes>`_ of the competition.

    * - year
      - integer
      - The year in which the competition started. For example, the ``year`` for a 16/17 competition would be 2016.

    * - current_matchday
      - integer
      - The competition's current matchday.

    * - number_of_matchdays
      - integer
      - The number of matchdays in this competition.

    * - number_of_teams
      - integer
      - The number of teams competing in this competition.

    * - number_of_games
      - integer
      - The number of games in this competition.

    * - last_updated
      - datetime
      - The date and time at which this resource was last updated.

LeagueTable
-------------

.. list-table::
    :widths: 40 40 100
    :header-rows: 1

    * - Attribute
      - Type
      - Description

    * - competition_id
      - integer
      - The competition ID for this league table.

    * - competition_name
      - string
      - The competition name for this league table.

    * - current_matchday
      - id
      - The current matchday.

    * - standings
      - list
      - A list of ``Standing`` objects. The list is one-indexed so as to correspond with the position in the table (i.e. standings[1] is the top of the table)

Standing
^^^^^^^^^^
Each ``Standing`` object represents a "row" in the league table. 

.. list-table::
    :widths: 40 40 100
    :header-rows: 1

    * - Attribute
      - Type
      - Description

    * - team_id
      - integer
      - The team ID.

    * - team_name
      - string
      - The team name.

    * - crest_url
      - string
      - A link to an image of the team's crest.

    * - position
      - integer
      - The current team's position.

    * - games_played
      - integer
      - The number of games played by this team.

    * - points
      - integer
      - The number of points that this team has.

    * - goals
      - integer
      - The number of goals scored by this team.

    * - goals_against
      - integer
      - The number of goals conceded by this team.

    * - goal_difference
      - integer
      - ``(goals - goals_against)``

    * - wins
      - integer
      - The number of wins this team has.

    * - draws
      - integer
      - The number of draws this team has.

    * - losses
      - integer
      - The number of losses this team has.

    * - home
      - dict
      - Contains ``goals``, ``goals_against``, ``wins``, ``draws``, and ``losses`` keys with integer values that represent home stats.

    * - away
      - dict
      - Contains ``goals``, ``goals_against``, ``wins``, ``draws``, and ``losses`` keys with integer values that represent away stats.



Fixture
---------

.. list-table::
    :widths: 40 40 100
    :header-rows: 1

    * - Attribute
      - Type
      - Description

    * - date
      - datetime
      - The fixture date and time.

    * - status
      - string
      - The status of this fixture.

    * - matchday
      - integer
      - The matchday on which this fixture is set.

    * - home_team
      - string
      - The name of the home team.

    * - home_team_id
      - integer
      - The ID of the home team.

    * - away_team
      - string
      - The name of the away team.

    * - away_team_id
      - integer
      - The ID of the away team.

    * - competition_id
      - integer
      - The ID of the competition for this fixture.

    * - result
      - dict
      - The result for this fixture. ``None`` if the match is not complete. Otherwise, contains ``home_team_goals`` and ``away_team_goals`` keys with integer values. Some ``Fixtures`` have a ``half_time`` key set for the score at half time.

    * - odds
      - dict
      - The betting odds for this fixture. ``None`` if not available. Otherwise, contains ``home_win``, ``draw`` and ``away_win`` keys with float values.

Team
------

.. list-table::
    :widths: 40 40 100
    :header-rows: 1

    * - Attribute
      - Type
      - Description

    * - id
      - integer
      - The team ID.

    * - name
      - string
      - The team name.

    * - code
      - string
      - The team code (e.g. Borussia Dortmund's code is BVB).

    * - short_name
      - string
      - The team's short name.

    * - market_value
      - string
      - The collective market value of the team's squad.

    * - crest_url
      - string
      - A link to an image of the team's crest.

Player
------

.. list-table::
    :widths: 40 40 100
    :header-rows: 1

    * - Attribute
      - Type
      - Description

    * - name
      - string
      - The player's name.

    * - position
      - string
      - The player's position on the field.

    * - jersey_number
      - integer
      - The player's kit number.

    * - date_of_birth
      - date
      - The player's date of birth.

    * - nationality
      - string
      - The player's nationality.

    * - contract_until
      - date
      - The date of the player's contract expiry with their team.

    * - market_value
      - string
      - The player's market value.