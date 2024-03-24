# words = ['radar', 'level', 'rotor', 'not palindrome']
#
#
# result = list(filter(lambda x: (x == "".join(reversed(x))), words))
#
# print(result)

my_list = ["rotor", "level", "radar", "mama"]

palindromes = filter(lambda word: word == word[::-1], my_list)

for palindrome in palindromes:
    print(palindrome)
