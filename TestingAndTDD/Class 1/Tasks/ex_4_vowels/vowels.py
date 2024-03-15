def vowels_count(text):
    amount_of_vowels = 0
    vowels = 'aeiou'
    for char in text:
        if char.lower() in vowels:
            amount_of_vowels += 1
    return amount_of_vowels


if __name__ == "__main__":
    user_input = "aaA www iii"
    print(vowels_count(user_input))

