numPlayers = int(input()) #N
goodPlayers = 0
add = ''
for p in range(numPlayers):
    points = int(input())
    fouls = int(input())
    stars = points*5 - fouls*3
    if stars > 40:
        goodPlayers += 1

if goodPlayers == numPlayers:
    add = '+'

print(str(goodPlayers) + add)