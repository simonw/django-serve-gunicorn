# django-serve-gunicorn

[![PyPI](https://img.shields.io/pypi/v/django-serve-gunicorn.svg)](https://pypi.org/project/django-serve-gunicorn/)
[![Changelog](https://img.shields.io/github/v/release/simonw/django-serve-gunicorn?include_prereleases&label=changelog)](https://github.com/simonw/django-serve-gunicorn/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/django-serve-gunicorn/blob/main/LICENSE)

Management command to start a gunicorn server for a Django project

## Installation

Install this library using `pip`:

    $ pip install django-serve-gunicorn

## Usage

Usage instructions go here.

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd django-serve-gunicorn
    python -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
