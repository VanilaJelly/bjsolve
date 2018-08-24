num_cases = input()
indexstr0 = "Data Set "
for i in range(num_cases):
    indexstr = indexstr0 + str(i+1) + ":"
    h = input()
    action = raw_input()

    l = len(action)
    for i in range(l):
        if h == 0:
            break
        if action[i] == 'b':
            h = h-1
        else:
            h = h+1
    print indexstr
    print h , "\n"


