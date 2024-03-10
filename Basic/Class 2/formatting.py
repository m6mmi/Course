print('Hello Mr. Eimantas, nice to meet you!')

title = 'Mr.'
name = 'Eimantas'

# + method
print('Hello ' + title + ' ' + name + ', nice to meet you!')

# coma
print('Hello', title, name, ', nice to meet you!')

# printf
print('Hello %s %s, nice to meet you!' % (title, name))

# f-string
print(f'Hello {title} {name}, nice to meet you!')

# str.format
print('Hello {} {}, nice to meet you!'.format(title, name))
print('Hello {title} {name}, nice to meet you!'.format(title=title, name=name))
print('Hello {1} {0}, nice to meet you!'.format(title, name))

# rounding
num = 109.123523265643564
print(f'{num:.3f}')
print(f'{round(num, 3)}')

