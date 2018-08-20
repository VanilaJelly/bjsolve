def solveproblem():
    presses = input()
    result = []
    max = 0
    for i in range(1000):
        result.append(0)
    for i in range(presses):
        throw = raw_input()
        throw = throw.split()
        first = int(throw[1])
        last = int(throw[2])
        if last > max:
            max = last
        for j in range(first, last):
            result[j] = result[j] + 1

    out = ''
    for i in range(max):
        if result[i] == 0:
            pass
        else:
            out = out + chr(result[i]+64)
    return out

answer = []
testcases = input()
for i in range(testcases):
    output = solveproblem()
    answer.append(output)

for i in range(testcases):
    print answer[i]
