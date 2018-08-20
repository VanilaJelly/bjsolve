n = input()

a = 0
b = 1

loop = n/2
for i in range(loop):
    a = a + b
    b = a + b

if n%2 == 0:
    print a
else:
    print b
