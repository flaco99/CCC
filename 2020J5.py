# work backwards?

# table = [
# [A, B, C, D]
# [E, F, G, H]
# [I, J, K, L]
# ]
#
# graph = {
#   [1,2] : [[],[]]
#   [3,4] : [[],[],[]]
#   [5,6] : [[]]
#   [7,8] : []
#   [7,8] : [[],[],[]]
#   [7,8] : [[],[],[]]
#   [7,8] : []
#   [7,8] : []
#   [7,8] : [[],[],[]]
#   [7,8] : [[],[]]
#   [7,8] : []
#   [7,8] : [[],[]]
# }

def getPositions(pos, r, c):
    num = vtable[pos[0]][pos[1]]
    positions = []
    for f in range(int(num/2)):
        if num % f == 0:
            cf = int(num/f)
            if f<=r and f<=c and cf<= r and cf<= c:
                if vtable[f][cf] == False:
                    positions.append([f, cf])
                    positions.append([cf, f])
                    vtable[f][cf] = True
    return(positions)

M = int(input()) # rows
N = int(input()) # columns

table = []
graph = {}

for r in range(M):
    iRow = input().split(' ')
    fRow = []
    for i in iRow:
        fRow.append()[int(i)] = False
    table.append(fRow)

for r in range(M):
    for c in range(N):
        position = [r,c]
        graph[position] : getPositions(position, M, N)
        # or is it graph[position] = getPositions(position, M, N)

position = [M,N]

cNum = table[position[0]][position[1]]

visited = [] # List to keep track of visited nodes.
queue = [] # Initialize a queue

def bfs(visited, graph, queue, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')

while position != [M,N]:
    numInP = table[position[0]][position[1]]
    allPos = getPositions(numInP)
    for pos in allPos:


