from django_serve_gunicorn import example_function


def test_example_function():
    assert example_function() == 2
