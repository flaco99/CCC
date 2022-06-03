T = input()
S = input()
i = 0
yon = 'no'

while (i <= len(S)) and (yon == 'no'):
    S = S[1:]+S[0]
    if S in T:
        yon = 'yes'
        print('yes')
    else:
        yon = 'no'
    i += 1
if yon == 'no':
    print('no')