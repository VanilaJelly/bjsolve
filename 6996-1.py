n = input()
a = ""

for i in range(n):
    l = raw_input().split()
    w = l[0]
    u = l[1]

    N = w + " & " + u + " are NOT anagrams."
    Y = w + " & " + u + " are anagrams."

    w = list(w)
    u = list(u)

    w.sort()
    u.sort()

    if w == u:
        a = a + Y
    else:
        a = a + N

    if i != n - 1:
        a = a + "\n"

print a
