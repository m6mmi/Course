def add_binary(a, b):
    return bin(a + b)[2:]


def add_bin(a, b):
    ans = ""
    number = a + b
    while number:
        ans += str(number & 1)
        number = number >> 1
    ans = ans[::-1]
    return ans
