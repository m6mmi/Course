def is_isogram(string):
    # Compare string length with set of character in string
    # Multiple same characters a
    return len(string) == len(set(string.lower()))
