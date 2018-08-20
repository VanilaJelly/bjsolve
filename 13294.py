import time


def bin(start, end, subj):
    m = (start+end)/2
    if fac(m) == subj:
        print m
    elif fac(m) > subj:
        bin(start, m, subj)
    else:
        bin(m+1, start, subj)

def fac(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

def process(subj):
    '''
    subj = input()
    '''
    start_time = time.time()
    str_subj = str(subj)
    count = 0
    str_subj = str(subj)
    l = len(str_subj)
    for i in range(l):
        if int(str_subj[l-i-1]) == 0:
            count = count + 1
        else:
            break

    start = 4 * count
    end = (start/5)*5+5

    bin(start, end, subj)
    end_time = time.time()
    consumed = end_time-start_time
    print consumed
    if consumed > 1:
        print "**************************************"


f=open("tc13294.txt", 'r')
lines = f.readlines()
for line in lines:
    process(int(line))
