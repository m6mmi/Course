def mumbling(text):
    # Create new empty string
    new_text = ''
    # Iterate through given characters and give each letter index
    for index, i in enumerate(text):
        # For each letter multiply it with index+1 and make a first letter capitalized
        new_text = new_text + ((index + 1) * i).capitalize() + '-'
    return new_text[:-1]
