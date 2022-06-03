S = int(input())
M = int(input())
L = int(input())

happiness = S + 2*M + 3*L

if happiness >= 10:
    print('happy')
else:
    print('sad')