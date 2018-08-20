import random

def maketestcase(size, i):
    numlist = []
    resultlist = []
    for i in range(size*size):
        numlist = numlist + [i+1]

#    random.shuffle(numlist)

    for i in range(size):
        resultlist.append([])
        for j in range(size):
            resultlist[i] = resultlist[i] + [numlist.pop()]


    f = open("testcases/testcase"+str(i)+".txt", 'w')

    f.write(str(size) + "\n")
    for j in range(size):
        line = ""
        for k in range(size):
            line = line +str(resultlist[j][k]) + " "
        f.write(line + "\n")

for i in range(1000):
    maketestcase(i, i)

