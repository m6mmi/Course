text = ("Python 3.2")

numbers = 0
letters = 0
other = 0

for i in text:
    if i.isnumeric():
        numbers += 1
    # elif i not in (" ", ".", ",","!"):
    #     letters += 1
    elif i.isalpha():
        letters += 1
    else:
        other += 1

print(f'Letters {letters}\n'
      f'Numbers {numbers}\n'
      f'Others {other}')
