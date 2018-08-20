def phi(num):
    if(num < 1):
	return 0
    if(num == 1):
	return 1
    if(num in self.primes_table):
	return num-1
    pfs = factorization2(num)
    prod = num
    for pfi in pfs:
	prod = prod*(pfi-1)/pfi
    return prod 


#prime factoring of n
def factorization(n):
    i = 2
    factorlist = []
    while i*i <= n:
        if n%i == 0:
            factorlist.append(i)
            n = n/i
            i = 1
        i=i+1
    factorlist.append(n)
    return factorlist

def factorization2(n):
    i = 2
    factorlist = {}
    while i*i <= n:
        if n%i == 0:
            factorlist.append(i)
            n = n/i
            i = 1
        i=i+1
    factorlist.append(n)
    return factorlist

#returns the number of i s.t gcd(i, n)=1
def pi(n):

    if n == 1:
        return 1

    factorlist = factorization(n)
    result = 1
    l = len(factorlist)
    i = 0

    while i < l:
        k = factorlist[i]
        kc = factorlist.count(k)
        if kc == 1:
            result = result * (k-1)
            i = i + 1
        else:
            result = result *k**kc - k**(kc-1)
            i = i + kc
    return result

n = input()
print pi(n), phi(n)
