text = ("Jelly-o donut tiramisu sugar plum pastry gummies liquorice macaroon. Chupa chups tootsie roll tootsie roll "
        "brownie powder cookie. Wafer dragée bonbon soufflé bear claw pudding oat cake apple pie gummies.")


def counter(u_input):
    import json
    words_counter = {}
    word_list = u_input.split()
    for word in word_list:
        if words_counter.get(word.strip(".")):
            print("In")
            words_counter[word.strip(".")] += 1
        else:
            print("Not in")
            words_counter[word.strip(".")] = 1
    print(json.dumps(words_counter, indent=4))


counter(text)
