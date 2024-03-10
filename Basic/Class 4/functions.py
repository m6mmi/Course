# Simple function, no return, no parameters
def test_function():
    print("Hello from the function")


# Simple function, returns sum of 2+2, no parameters
def calculator():
    print("Calculator")
    sum_of_two = 2 + 2
    return sum_of_two
    # print function that will never run as it is unreachable
    print("Hello from the function")


# Complex function, no parameters, returns value
# True condition will be returned
def conditional():
    if 2 > 3:
        return "Yes"
    else:
        return "No"


def better_conditional(number=0):
    if number < 18:
        return "Go Home"
    return "You can come in"  # no need else condition in this case.
    # if number < 18 is false then function will continue


# Has parameters, returns value(sum)
def calculator_2(number1, number2):
    sum = number1 + number2
    return sum


print(calculator_2(3,4))
# test_function()
#print(better_conditional())
#print(better_conditional(calculator_2(5, 20)))  # hard to read
# result = calculator()
# print(result)
# print(conditional())
