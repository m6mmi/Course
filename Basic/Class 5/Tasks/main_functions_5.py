# String reversal
def string_reverse(text):
    return text[::-1]


# Palindrome Checker: Create a function that checks if a given string is a palindrome
# (reads the same backward as forward).
# Use this function to check whether a user-inputted string is a palindrome.
def palindrome(text):
    # reverse text
    reversed_text = text[::-1]
    # check if entered text is equal to reversed text and return result
    result = "palindrome" if text == reversed_text else "not palindrome"
    return print(f"Entered text is {result}.")


# count each word
#  use dictionary to store the words count
#  allow user to input a sentence and display word count result
def word_count(text):
    # change all text lowercase so Text and text is same
    text = text.lower()
    # create empty dictionary
    dict = {}
    # result to return from function

    for i in text.split():
        # add word do dictionary and if word is in dictionary then add only +1
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    # print each word and its count
    for key, value in dict.items():
        print(f'{key} = {value} times.')
    # return value There is {len(text.split())} words in sentence.
    return print(f'There is {len(text.split())} words in sentence.')


# check if two word are anagrams
def anagram(text1, text2):
    # create lists and change all letters to lowercase
    text1_list = list(text1.lower())
    text2_list = list(text2.lower())
    # sort all letters in list
    text1_list.sort()
    text2_list.sort()
    # compare two words
    result = "are anagrams" if text1_list == text2_list else "are not anagrams"
    # return result print
    return print(f"{text1} and {text2} {result}")


# replace " " with "_" and lowercase all
def string_manipulation(text):
    text = text.replace(" ", "_")
    return print(text.lower())


# get sum avg max min
def list_operation(n_list):
    # remove "," if there is any and create list
    n_list = n_list.replace(",", "").split()
    # convert list strings to integers
    n_list = [int(i) for i in n_list]
    # return print result
    return print(f"list = {n_list}\n"
                 f"SUM: {sum(n_list)}\n"
                 f"AVG: {round(sum(n_list) / len(n_list), 2)}\n"
                 f"MAX: {max(n_list)}\n"
                 f"MIN: {min(n_list)}")