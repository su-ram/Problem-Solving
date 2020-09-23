import sys
import copy

sys.stdin = open('./../../input.txt.txt', 'r')

n = int(input())

matrix = []
highest = -1

def DFS(start, limit):

    stack = [start]

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]


    while stack :

        node = stack.pop()
        x , y = node[0], node[1]
        visited[x][y] = 1

        for k in range(4):
            x2 = x + dx[k]
            y2 = y + dy[k]

            if 0 <= x2 < n and 0 <= y2 < n:
                if clone[x2][y2] > limit and visited[x2][y2] == 0 :
                    stack.append((x2,y2))
    return 1


for _ in range(n):
    arr = list(map(int, input().split()))
    maxnum = max(arr)
    if highest < maxnum:
        highest = maxnum
    matrix.append(arr)
    
candidate = set()

for i in range(1, maxnum+1):
    clone = copy.deepcopy(matrix)
    
    visited = [[0]*n for _ in range(n)]
    total = 0 

    for x in range(n):
        for y in range(n):
            if clone[x][y] > i and visited[x][y] == 0 :
                total += DFS((x,y), i)
    if total == 0 : total = 1 # .....................한 번도 호출이 되지 않았다는 의미 
    candidate.add(total)
print(max(candidate))


