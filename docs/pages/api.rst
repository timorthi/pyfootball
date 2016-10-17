API
====

For every function that sends a HTTP request, an ``HTTPError`` is raised whenever the response status code is ``4XX`` or ``5XX`` which signifies that something went wrong between pyfootball sending the API a request and the API giving a response. If you believe this to be an issue with pyfootball itself, please see :doc:`support` for more information.

Football
----------
This class serves as the driver/entry point for this library.

.. automodule:: pyfootball.football
.. autoclass:: Football
    :members:

    .. automethod:: __init__

Competition
-------------

.. automodule:: pyfootball.models.competition
.. autoclass:: Competition
    :members:

Team
-----

.. automodule:: pyfootball.models.team
.. autoclass:: Team
    :members: