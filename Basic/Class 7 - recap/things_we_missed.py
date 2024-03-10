# print("Hello world")
# text = 'hello world'
# print(f'{text}')
# print('hello world', text)
#
# variable1: int = 5  # integer
# variable2: str = "some text value enter"  # string
# variable3: float = 15.123  # float
# variable4: bool = True  # boolean
#
# # integer(int), float, string(str), boolean(bool) , None, undefined
#
# # getting variable type
# print(type(variable1))
# print(type(variable4))
# print(type(variable2))
# print(type(variable3))
#
# print(f"{'Hello':_^11}")
# print(f"{'Hello':_<11}")
# print(f"{'Hello':_>11}")
#
# print(f"{len(variable2)}")
# print(variable2.split())
#
# for word in variable2.split():
#     print(word.strip('e'))
#
# new_words = []  # initiate a new list
# for word in variable2.split():  # iterate trough words
#     new_words.append(word.strip('e'))
# print(new_words)
# new_text = ' '.join(new_words)  # converting a list to text
# print(new_text)
#
# list_variable = []
# dictionary = {}
# dictionary = {'key': 'value'}
# # dictionary = {'key': ['key': [{'key': 'value'}, {'key': 'value', 'key': 'value'}]]}
#
#
# user_choice = input("Choose what to do: ")
# print(user_choice)
#
# # 0 , '', null, undefined, False, [], {} = Falsy
# # 1, ' ', [0], {'key': 'value'} = Truthy
#
# if user_choice:
#     print("This happen")
#
#
# if user_choice:
#     print("do True case things")
# elif user_choice == "potato":
#     print("Estonian gold")
# else:
#     print("Do whatever for not accounts cases")
#
#
# iterable_text = "asdasdasdasdasdasdasdasd"
#
# for letter in iterable_text:
#     print(letter)
#
# while True:
#     number = int(input("Number: "))
#     if number > 5:
#         break
#

# def function_name(text):
#     print("This is function!")
#     print(text)
#
#
# function_name('Janek')

def function_name(*args):
    print(args)
    sum = 0
    for arg in args:
        sum += arg
    print(sum)


function_name(1, 2, 3, 4, 5)



