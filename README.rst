pyfootball
============
.. image:: https://readthedocs.org/projects/pyfootball/badge/?version=latest
    :target: http://pyfootball.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/xozzo/pyfootball.svg?branch=develop
    :target: https://travis-ci.org/xozzo/pyfootball
    :alt: Travis CI Status

pyfootball is a client library for `football-data.org <http://api.football-data.org/index>`_ written in Python.

You can familiarize yourself with pyfootball's API with the `documentation <https://pyfootball.readthedocs.io>`_.

Requirements
---------------

* A valid API key for football-data. You can request for one at `<http://api.football-data.org/register>`_.
* Python 3.5+
* The ``requests`` library. pip should handle this for you when installing pyfootball.

Installation
---------------
::

    pip install pyfootball

Example Usage
------------------
::

    >>> import pyfootball
    >>> f = pyfootball.Football(api_key='your_api_key')
    >>> bayern = f.get_team(5)
    >>> bayern.market_value
    582,225,000 €

Support
----------
If you encounter any bugs, please let me know by `creating an issue <https://github.com/xozzo/pyfootball/issues/new>`_ or tweeting at me `@timorthi <https://www.twitter.com/timorthi>`_.  

Contributing
---------------
Please see the repository's `CONTRIBUTING` file.

License
----------
The project is licensed under the MIT license.
