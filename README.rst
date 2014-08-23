
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