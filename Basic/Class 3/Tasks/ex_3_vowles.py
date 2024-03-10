text = input("Enter text to count vowels: ")
#text = "This is text for fast test !!!"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
a = 0
e = 0
i = 0
o = 0
u = 0
other = 0

for char in text.lower():
    if char in vowels:
        count += 1
    match char:
        case "a":
            a += 1
        case "e":
            e += 1
        case "i":
            i += 1
        case "o":
             o += 1
        case "u":
            u += 1
        case _:
            other += 1



print(f'This text have {count} vowels')
print(f'a = {a}\n'
      f'e = {e}\n'
      f'i = {i}\n'
      f'o = {o}\n'
      f'u = {u}\n'
      f'other = {other}')