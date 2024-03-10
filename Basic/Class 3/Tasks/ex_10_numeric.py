text = ("Python 3.2")

numbers = 0
letters = 0

for i in text:
    if i.isnumeric():
        numbers += 1
    elif i not in (" ", ".", ",","!"):
        letters += 1

print(f'Letters {letters}\n'
      f'Numbers {numbers}')
