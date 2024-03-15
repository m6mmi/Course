import pytest

from fibonacci import fibonacci


@pytest.mark.parametrize("number, result", [(10, 55), (2, 1), (5, 5), (100, 354224848179261915075)])
def test_fibonacci(number, result):
    """ Test if return is correct fibonacci number """
    assert fibonacci(number) == result
