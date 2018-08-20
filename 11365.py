line = raw_input()
while line != "END":
    line = list(line)
    line.reverse()
    print ''.join(line)
    line = raw_input()
