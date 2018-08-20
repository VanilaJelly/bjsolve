def poww(n, times):
    p = 1
    for i in range(times):
        p = p * n
    return p

def logg(n):
    p = 1
    for i in range(1, 100000):
        p = p * n
        if (p > 10000000000):
            return i * 100
    return -1

def numrep(n, a):
    result = 0
    p = 1
    while n > 0:
        temp = n % a
        temp = temp * p
        p = p * 10
        result = result + temp
        n = n / a
    return result

def nth(n, a):
    m = logg(a)
    temp = a
    i = 0
    for i in range(m):
        if n < temp:
            break
        temp = temp * a

    j = 0

    p = poww(a, i)
    while j < (i+1)/2:
        temp1 = n % a
        temp2 = n / p
        if temp1 != temp2:
            break;
        n = n - temp2 * p
        n = n / a
        j = j + 1
        p = p / (a*a)

    if j == (i+1)/2:
        return 1;

    return 0

k = input()
count = 0
for i in range(2, 11):
    result = nth(k, i)
    print numrep(k, i)
    if result == 1:
        count = count + 1
        print i, numrep(k, i)

if count == 0:
    print "NIE"
