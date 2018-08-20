s = input()
i = 0
while s > 0:
    q = 5
    c = 0
    while q <= s:
        s = s / q
        c = c + s
    s = input()
    i = i + 1
    print "Case #"+str(i)+":", c
