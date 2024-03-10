text = "Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love"

new_text = ""

for index, char in enumerate(text):
    index += 1
    if index % 3 == 0:
        char = char.upper()
    elif index % 4 == 0:
        char += "!"
    new_text += char
print(new_text)
