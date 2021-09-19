from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="django-serve-gunicorn",
    description="Management command to start a gunicorn server for a Django project",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/django-serve-gunicorn",
    project_urls={
        "Issues": "https://github.com/simonw/django-serve-gunicorn/issues",
        "CI": "https://github.com/simonw/django-serve-gunicorn/actions",
        "Changelog": "https://github.com/simonw/django-serve-gunicorn/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["django_serve_gunicorn"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    tests_require=["django-serve-gunicorn[test]"],
    python_requires=">=3.6",
)
