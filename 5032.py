inp = raw_input()

lt = inp.split()

e = int(lt[0]) + int(lt[1])
c = int(lt[2])
drink = 0

while e >= c:
    new = e / c
    drink = drink + new
    e = (e % c) + new

print drink

