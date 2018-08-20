size = raw_input().split()
n = int(size[0])
m = int(size[1])

ncase = input()

rows = []
for i in range(n):
    rows.append(raw_input())

cases = []
for i in range(ncase):
    cases.append(raw_input().split())

result = ""

for case in cases:
    O = 0
    J = 0
    I = 0
    for i in range(4):
        case[i] = int(case[i])
    for i in range(case[0]-1, case[2]):
        for j in range(case[1]-1, case[3]):
            if rows[i][j] == 'O':
                O = O + 1
            elif rows[i][j] == 'J':
                J = J + 1
            else:
                I = I + 1

    result = result + str(J) + " " + str(O) + " " + str(I)
    if case != cases[ncase-1]:
        result = result + "\n"

print result
