import vowels


def test_vowels_count_1(text_2):
    assert vowels.vowels_count(text_2) == 102


def test_vowels_count_2(text_1):
    assert vowels.vowels_count(text_1) == 6
