import pytest

import century


@pytest.mark.parametrize("year, result", [(2014, 'You are in the 21 century'),
                                          (-1, "Nice! You are not even in a first century yet!"),
                                          (1995, 'You are in the 20 century')])
def test_get_century(year, result):
    """ Test if year returns correct century and text """
    assert century.get_century(year) == result
