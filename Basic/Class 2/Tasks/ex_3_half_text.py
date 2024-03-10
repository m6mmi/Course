# split text
# we ask user to input text
text = input('Please insert some text: ')
# lets look long is text
text_length = len(text) + 1
# lest split text in to 2 half's
text_mid_point = text_length // 2
text_1 = text[0: text_mid_point]
# second part of text reversed
text_2 = text[:text_mid_point-1:-1]
# print out first half ok and last reversed
print(f'{text_1}{text_2}')