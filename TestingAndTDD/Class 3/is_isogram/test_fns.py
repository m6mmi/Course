# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
#
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

import fns

def test_is_isogram():
    assert fns.is_isogram("Dermatoglyphics") == True
    assert fns.is_isogram("isogram") == True
    assert fns.is_isogram("aba") == False
    assert fns.is_isogram("moOse") == False
    assert fns.is_isogram("isIsogram") == False
    assert fns.is_isogram("") == True