def word_play(text):
    text_list = enumerate(text)
    final_string = ""

    for index, char in text_list:
        if (index + 1) % 3 == 0:
            final_string += (char.upper())
        elif (index + 1) % 4 == 0:
            final_string += f"{char}!"
        else:
            final_string += char
    return final_string


if __name__ == "__main__":
    user_input = "Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love"
    print(word_play(user_input))
