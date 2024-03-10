print("Some random stuff.")
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

# (x + y + z)(x2 + y2 + z2 – xy – yz -xz)
c = (x + y + z)*(x**2 + y**2 + z**2 - x*y - y*z - x*z)

### wrong way
### x2 + y2 + z2 – 3xyz
### d = x**2 + y**2 + z**2 - 3*x*y*z
print('Some random answer: ', c)
