import fns

def test_get_middle():
    assert fns.get_middle("test") == "es"
    assert fns.get_middle("testing") == "t"
    assert fns.get_middle("middle") == "dd"
    assert fns.get_middle("A") == "A"
    assert fns.get_middle("of") =="of"
