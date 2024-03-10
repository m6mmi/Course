# Algebra monter
# a**3 - b**3
# formula: (a-b)(a2+ab+b2)

print('ALGEBRA MONSTER')
while True:
    a = input('Enter a = ')
    try:
        a = int(a)
        break
    except ValueError:
            print('Must be integer  !!!')

while True:
    b = input('Enter b = ')
    try:
        b = int(b)
        break
    except ValueError:
            print('Must be integer  !!!')

c = (a-b)*(a**2 + a*b + b**2)

print("Algebra montser says:", c)