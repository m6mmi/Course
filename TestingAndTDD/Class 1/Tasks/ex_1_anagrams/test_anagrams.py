import pytest

from anagrams import is_anagrams


@pytest.mark.parametrize("text_1, text_2, result", [('kert', 'retk', True), ('dog', 'god', True), ('cat', 'mouse', False)])
def test_is_anagrams(text_1, text_2, result):
    """ Test if two words are anagrams and function returns True or False """
    assert is_anagrams(text_1, text_2) is result
