import pytest

from is_prime import is_prime


@pytest.mark.parametrize("n, result", [(4, False), (11, True), (34, False), (5, True)])
def test_is_prime(n, result):
    """ Test if prime number is True or False """
    assert is_prime(n) == result
