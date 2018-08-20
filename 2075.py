def getinput(size, columns):
    size = input()

    for i in range(size):
        columns.append([])

    for i in range(size):
        row = raw_input()
        row = row.split()
        for j in range(size):
            columns[j].append(row[j])
    return size


def process(size, columns):
    finding = [columns[size-1].pop()]
    if not columns[size-1]:
        columns.remove(columns[size-1])
    index = 1

    while index < size:
        for column in columns:
            subject = column.pop()
            for i in range(index):
                if int(finding[index-i-1]) >= int(subject):
                    l1 = finding[:index-i]
                    l2 = finding[index-i:size-1]
                    l1.append(subject)
                    finding = l1+l2
                    break
                elif i == index - 1:
                    l1 = []
                    l1.append(subject)
                    finding = l1 + finding
                    break
            if not column:
                columns.remove(column)
            index = index + 1
            if index == size:
                break


    while columns:
        for column in columns:
            subject = column.pop()
            if int(subject) <= int(finding[size-1]):
                columns.remove(column)
                continue
            else:
                for i in range(index+1):
                    if int(finding[index-i-1]) >= int(subject):
                        l1 = finding[:index-i]
                        l2 = finding[index-i:size-1]
                        l1.append(subject)
                        finding = l1+l2
                        break
            if not column:
                columns.remove(column)

    return finding[size-1]

size = 0
columns = []
size = getinput(size, columns)
print process(size, columns)
