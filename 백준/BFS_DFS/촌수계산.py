n = int(input())
p1, p2 = map(int, input().split())
relations = int(input())
visited=[0]*(n+1)
matrix = [[0]*(n+1) for _ in range(n+1)]
total = 0
for i in range(relations):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
def getList(num):
    result = []
    for i in range(n):
        if matrix[num][i] == 1:
            result.append(i)
    return result

def DFS(num,cnt):
    if num == p2:
        global total
        total = cnt
        return total
    else:
        visited[num] = 1

    for i in range(n+1):
        index = matrix[num][i]
        if index == 1 and visited[i] == 0 :
            DFS(i, cnt + 1)


DFS(p1, 0)
print(total)


