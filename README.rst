dojo
====

coding for fun and profit ...

.. image:: https://travis-ci.org/thoreg/dojo.svg?branch=master
  :target: https://travis-ci.org/thoreg/dojo
.. image:: https://coveralls.io/repos/thoreg/dojo/badge.png
  :target: https://coveralls.io/r/thoreg/dojo



Setup
-----

.. code:: bash

    mkvirtualenv dojo
    pip install -r requirements.txt


Development Server
------------------

.. code:: bash

    # export PYTHONPATH to the directory where 'dojo' exists
    python views.py


Tests
-----

.. code:: bash

    # Run all tests
    make tests

    # Run continuous all tests (used during test driven development)
    make tdd

    # Run acceptance tests
    make behave
