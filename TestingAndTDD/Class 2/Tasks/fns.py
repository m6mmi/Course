def add(a, b):
    return a + b


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    return True if text[::-1] == text else False


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact


def find_max(num_list):
    if not num_list:
        return None

    return max(num_list)


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def remove_duplicates(num_list):
    new_list = []
    for i in num_list:
        if i not in new_list:
            new_list.append(i)

    return new_list


def are_anagrams(first, second):
    if sorted(first) == sorted(second):
        return True
    return False


def celsius_to_fahrenheit(tempC):
    tempF = (tempC * 1.8) + 32

    return tempF
