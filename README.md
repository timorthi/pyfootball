# pyfootball
[![Documentation Status](https://readthedocs.org/projects/pyfootball/badge/?version=latest)](http://pyfootball.readthedocs.io/en/latest/?badge=latest)  

pyfootball is a client library for [football-data.org](http://api.football-data.org/index) written in Python.

You can familiarize yourself with pyfootball's API with the [documentation](https://pyfootball.readthedocs.io).

#Requirements
* A valid API key for football-data. You can request for one [here](http://api.football-data.org/register).
* Python 3.5+
* The ``requests`` library. pip should handle this for you when installing pyfootball.

## Installation
    pip install pyfootball

## Example Usage
    >>> import pyfootball
    >>> f = pyfootball.Football('your_api_key')
    >>> bayern = f.get_team(5)
    >>> bayern.market_value
    582,225,000 €

## Support
If you encounter any bugs, please let me know by [creating an issue](https://github.com/xozzo/pyfootball/issues/new) or tweeting at me [@timorthi](https://www.twitter.com/timorthi).

## License
The project is licensed under the MIT license.