P = int(input())
N = int(input())
R = int(input())

infected = N
total = infected
days = 0
while total <= P:
    days += 1
    infected = infected*R
    total += infected

print(days)