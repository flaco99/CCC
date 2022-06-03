def getcords(instr):
    xdone = False
    X = ''
    Y = ''
    for char in instr:
        if char == ',':
            if xdone is False:
                xdone = True
            else:
                Y += char
        else:
            if xdone is False:
                X += char
            else:
                Y += char
    clist = [int(X), int(Y)]
    return clist

N = int(input())
dotCin = input()
dotCin = getcords(dotCin)
dotX = int(dotCin[0])
dotY = int(dotCin[1])
boxBX = dotX
boxBY = dotY
boxTX = dotX
boxTY = dotY

for i in range(N-1):
    dotCin = input()
    dotCin = getcords(dotCin)
    dotX = int(dotCin[0])
    dotY = int(dotCin[1])
    if dotX >= boxTX:
        boxTX = dotX
    if dotX <= boxBX:
        boxBX = dotX
    if dotY >= boxTY:
        boxTY = dotY
    if dotY <= boxBY:
        boxBY = dotY

print(f'{boxBX-1},{boxBY-1}')
print(f'{boxTX+1},{boxTY+1}')