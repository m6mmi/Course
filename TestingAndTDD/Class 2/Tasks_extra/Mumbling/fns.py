def mumbling(text):
    new_text = ''
    for index, i in enumerate(text):
        new_text = new_text + ((index + 1) * i).capitalize() + '-'
    new_text.rstrip('-')
    return new_text[:-1]
