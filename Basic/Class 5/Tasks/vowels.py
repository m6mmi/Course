vowels = 'aeiou'
text = "aaa www iii"
amount_of_vowels = 0

for char in text:
    if char.lower() in vowels:
        amount_of_vowels += 1

print(amount_of_vowels)

