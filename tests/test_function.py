"""Test the python function from src."""

from src.function import my_function


def test_function() -> None:
    """See it the function really returns true."""
    assert my_function() is True
