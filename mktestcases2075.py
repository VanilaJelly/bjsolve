import random

def generator(n):
    tosort = []
    filename = "testcases/testcase" + str(n) + ".txt"
    f = open(filename, 'w')
    size = random.randint(1, 1500)
    f.write(str(size) + "\n")
    for i in range(size):
        line = ""
        new = 0
        for j in range(size):
            new = new + random.randint(1, 4000000000/size)
            line = line + " " + str(new)
            tosort.append(new)
        f.write(line + "\n")

    tosort.sort()
    tosort.reverse()
    answer = tosort[size-1]
    f.write(str(answer))

for i in range(100):
    generator(i)
