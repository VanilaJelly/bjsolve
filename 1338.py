#unknown number 170530


def findnum():
    line1 = raw_input()
    line2 = raw_input()

    line1 = line1.split()
    line2 = line2.split()

    cand1 = int(line1[0])
    cand2 = int(line1[1])


    quotient = int(line2[0])
    remainder = int(line2[1])

    if cand1 > cand2:
        start = cand2
        end = cand1
    elif cand1 < cand2:
        start = cand1
        end = cand2
    else:
        if cand1 % quotient == remainder:
            print cand1

    remainder = remainder % quotient

    if end-start >= 2 * quotient + 1:
        print "Unknwon Number"
        return

    if end-start >= quotient:
        for i in range(start, end-1-quotient):
            if i % quotient == remainder:
                print "Unknwon Number"
                return


    toadd = remainder - start%quotient
    if toadd < 0:
        toadd = toadd + quotient
    print start + toadd

findnum()

