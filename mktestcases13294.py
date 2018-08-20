def fac(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

f = open("tc13294.txt", 'w')

i = 100000
while i > 0:
    print i
    line = str(fac(i))
    l = len(line)
    print "len: ",l
    if i > 100010:
        break
    if l > 1000000:
        break
    f.write(str(line)+"\n")
    i = i + 1

