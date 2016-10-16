pyfootball
============
pyfootball is a client library for `football-data.org <http://api.football-data.org/index>`_ written in Python.

This library was written to allow for easier access to football-data's resources by abstracting HTTP requests and representing the JSON responses as Python classes.

**WARNING:** pyfootball *does not* rate limit methods that send HTTP requests to football-data's endpoints. You are responsible for adhering to the 50-requests-per-minute rule.

Requirements
-------------
* A valid API key for football-data. You can request for one `here <http://api.football-data.org/register>`_.
* Python 3.5+


Example Usage
--------------
    >>> import pyfootball
    >>> f = pyfootball.Football('your_api_key')
    >>> bayern = f.get_team(5)
    >>> bayern.market_value
    582,225,000 €

Table of Contents
------------------
.. toctree::
    :maxdepth: 1

    pages/getting_started.rst