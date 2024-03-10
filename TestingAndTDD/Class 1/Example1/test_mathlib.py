import mathlib


def test_addition():
    """ Testing addition """
    assert mathlib.addition(2, 3) == 5
    assert mathlib.addition(1, -4) == -3
    assert type(mathlib.addition(1, 2)) == int


def test_multiply():
    """ Testing multiplication functionality """
    assert mathlib.multiply(2, 2) == 4
    assert mathlib.multiply(2, -2) == -4
    assert type(mathlib.multiply(1, 3)) == int


def test_text():
    """ Testing if the letter is in the text """
    assert 'a' in 'Python Basic'
