import fns


def test_what_quarter():
    assert fns.what_quarter(3, 1)
    assert fns.what_quarter(8, 3)
    assert fns.what_quarter(11, 4)
