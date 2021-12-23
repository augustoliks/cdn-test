.. image:: https://badge.fury.io/py/cdn-test.svg
    :target: https://badge.fury.io/py/cdn-test

.. image:: https://travis-ci.com/augustoliks/cdn-test.svg?branch=main
    :target: https://travis-ci.com/github/augustoliks/cdn-test

cdn-test
========

CLI tool created to automate tests for verify time cache in web-site delivered by CDN - CloudFront.

How to Install
--------------

The ``cdn-test`` package is hosted in Python Package Index (PyPI). To
install ``cnd-test``, it's recommend create a ``virtualenv`` and install the package using ``pip``. Example:

.. code-block:: bash

    $ virtualenv --python=$(which python3) venv
    $ source venv/bin/activate
    $ pip3 install cdn-test

Manual
------

.. code-block:: bash

    $ cdn-test -h

    usage: cli.py [-h] [--url URL] [--time-step [TIME_STEP]] [--http-verb [HTTP_VERB]] [--header-name [HEADER_NAME]] [--output-file [OUTPUT_FILE]] [--version]

    options:
      -h, --help            show this help message and exit
      --url URL, -u URL     URL to verified cache in cloudfront
      --time-step [TIME_STEP], -s [TIME_STEP]
                            time interval between requests
      --http-verb [HTTP_VERB], -x [HTTP_VERB]
                            HTTP verb utilized for requests to URL
      --header-name [HEADER_NAME]
                            response header name that contains "Miss from cloudfront" or "Hit from cloudfront"
      --output-file [OUTPUT_FILE], -f [OUTPUT_FILE]
                            file path to save records
      --version, -v         show cdn-test version

Examples
--------

Each 10 seconds, it will be made a request with ``GET`` HTTP verb to web-site hosted by cloudformation with follow URL ``https://aws.amazon.com/pt/cloudfront/``. The request history will be save on ``~/cdn-report.json``.

.. code-block:: bash

    $ cdn-test --url=https://aws.amazon.com/pt/cloudfront/ --http-verb=GET --time-step=10s --output-file=~/cdn-report.json

Package Struct
--------------

.. code-block:: bash

    ├── src
    │   ├── cdn_test            # source code directory
    │   ├── __init__.py         # module definition file
    │   ├── cli.py              # parser cli parameters
    │   └── domain.py           # module composed only domain logics
    ├── poetry.lock             # poetry dependencies versions
    ├── pyproject.toml          # poetry package definition file
    ├── README.rst              # project documentation
    └── tests                   # directory composed only with unit tests
        └── ...
