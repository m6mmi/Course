example_text = 'Blood type is Beer!'

# Length
length = len(example_text)
print(length)

# What is the index of this character(first one)
print(f"Index of letter 'y' in the text is {example_text.index('y')}")

# What is the amount of certain letters in text
print(f"Amount of letter 'B' in the text is {example_text.count('B')}")
print(f"Amount of letter 'B' in the text is {example_text.count('B', 7)}")
print(f"Amount of letter 'B' and 'e' in the text is {example_text.count('B') + example_text.count('e')}")

# What is the character at the inidex 6
print(f"The character at index 6 is '{example_text[6]}'.")

# What are the character at the index range
print(f"The text in the range 6 -13 is '{example_text[6:13]}'")
print("The text in the range 6 -13 is",example_text[6:13])

# What are the every second character in the index range
# text[from:to:step]
print(f"The text in the range 6 -13 is '{example_text[6:13:1]}'")
print(f"The text in the range 6 -13 is '{example_text[::2]}'")

# String reversed
print(f"Reversed string '{example_text[13:6:-1]}'")

# Upper / Lower case
print(example_text.lower())
print(example_text.upper())

# Capitalize first letter
print(example_text.capitalize())

# Replace letter
print(example_text.replace('B', 'V'))


