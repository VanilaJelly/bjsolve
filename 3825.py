def ifprime(m, n):
    print m, n
    square = m**2 + n**2
    loop = square*(square+1)/2
    print loop
    for i in range(loop):
        divider = sqaresplit[i]
        if square % divider == 0:
            print "C"
            return
    print "P"

ntestcase = input()

varlist = []
max = 0
for i in range(ntestcase):
    temp = raw_input()
    varlist = varlist + temp.split()
    candid = int(varlist[2*i])**2 + int(varlist[2*i+1])**2
    if candid > max:
        max = candid

sqaresplit = []
for i in range(1, max):
    for j in range(1, i):
        sqaresplit.append(i**2 + j**2)

for i in range(ntestcase):
    m = int(varlist[2*i])
    n = int(varlist[2*i+1])
    ifprime(m, n)

