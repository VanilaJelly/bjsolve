inp = raw_input()

inp = inp.split()

a = int(inp[0])
b = int(inp[1])

result = 1
for i in range(a, b+1):
    tomult = i*(i+1)/2
    result = (result * tomult) % 14579

print result
