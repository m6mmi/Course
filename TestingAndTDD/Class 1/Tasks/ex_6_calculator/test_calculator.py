import pytest

from calculator import calculator


@pytest.mark.parametrize("operator, a, b, result", [("+", 2, 3, 5), ("*", 5, 5, 25), ("/", 100, 4, 25)])
def test_calculator(operator, a, b, result):
    """ Test if operator and two numbers return the correct answer """
    assert calculator(operator, a, b) == result
