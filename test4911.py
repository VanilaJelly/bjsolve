'''
print array
rotating rings
17/05/31
'''
def arrintoring(rows, cols, size):
    rings = []
    numrings = (size+1)/2
    for j in range(numrings-1):
        rings.append([])
        k = size-j-1
        rings[j] = rings[j] + rows[j][j:k]
        rings[j] = rings[j] + cols[k][j:k]
        toadd = rows[k][size-k:k+1]
        toadd.reverse()
        rings[j] = rings[j] + toadd
        toadd = cols[j][size-k:k+1]
        toadd.reverse()
        rings[j] = rings[j] + toadd
    j = numrings - 1
    if size % 2 == 1:
        rings.append([])
        rings[j] = rings[j] + [rows[j][j]]
    else:
        rings.append([])
        k = size-j-1
        rings[j] = rings[j] + rows[j][j:k]
        rings[j] = rings[j] + cols[k][j:k]
        toadd = rows[k][size-k:k+1]
        toadd.reverse()
        rings[j] = rings[j] + toadd
        toadd = cols[j][size-k:k+1]
        toadd.reverse()
        rings[j] = rings[j] + toadd
    return rings

def rowsintocols(rows, size):
    cols = []
    for i in range(size):
        cols.append([])
    for i in range(size):
        for j in range(size):
            cols[j] = cols[j] + [rows[i][j]]
    return cols

def makesortedring(size):
    value = 1
    array = []
    cols = []
    ring = []
    for i in range(size):
        array.append([])
        for j in range(size):
            array[i].append(value)
            value = value + 1

    cols = rowsintocols(array, size)
    ring = arrintoring(array, cols, size)
    return ring

def comparerings(sring, ring, size):
    subj = ring[0]
    result = 0
    start = -1
    for i in range(size):
        if sring[i] == subj:
            start = i
            break

    if start == -1:
        return -1

    for i in range(size):
        index = (start + i) % size
        if sring[index] != ring[i]:
            result = -1
    if i == size:
        result = 0
    return result

def process(size, f):

    rings = []
    rows = []
    cols = []

    for i in range(size):
        row = f.readline()
        row = row.split()
        for i in range(size):
            row[i] = int(row[i])
        rows.append(row)

    cols = rowsintocols(rows, size)

    rings = arrintoring(rows, cols, size)
    sortedrings = makesortedring(size)

    numrings = (size+1)/2


    result = 0

    if size % 2 == 0:
        for i in range(numrings):
            k = numrings - i - 1
            ringsize = 8 * k + 4
            result = result + comparerings(sortedrings[i], rings[i], ringsize)

    else:
        for i in range(numrings):
            k = numrings - i - 1
            ringsize = 8 * k
            if k == 0:
                ringsize = 1
            result = result + comparerings(sortedrings[i], rings[i], ringsize)

    return result


i = 1
answer = ""
while i < 168:
    f = open("testcases/testcase"+str(i-1)+".txt")
    size = int(f.readline())
    if size == 0:
        break
    elif i > 1:
        answer = answer + "\n"

    if size == 1:
        result = 0
    else:
        result = process(size, f)
    if result == 0:
        answer = answer + str(i)+". "+"YES"
    else:
        answer = answer + str(i)+". "+"NO"
    i = i + 1

print answer
