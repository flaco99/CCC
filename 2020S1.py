N = int(input())
myDict = {}
for i in range(N):
    TX = input()
    if TX == "":
        break
    TX = TX.split(' ')
    T = int(TX[0])
    X = int(TX[1])
    myDict[X] = T

myList = sorted(myDict, key=myDict.get)

speeds = []
for j in range(N-1):
    distance = abs(myList[j] - myList[j+1])
    t1 = myDict[myList[j]]
    t2 = myDict[myList[j+1]]
    time = t2 - t1
    speed = distance/time
    speeds.append(speed)

print(max(speeds))

# ccc grader didn't conduct subtask 8. is it because its not rounded to the nearest 10^-5?