n, m = map(int, input().split())
limit = min(n,m)
matrix = [ list(input()) for _ in range(n)]
max_area = 1
def square_check(start):
    x, y = start
    global max_area
    for i in range(limit):
        if x + i >= n or y + i >= m :
            continue
        if matrix[x][y] == matrix[x][y+i] == matrix[x+i][y] == matrix[x+i][y+i]:
            max_area = max(max_area, (i+1) ** 2)

for i in range(n):
    for j in range(m):
        square_check((i,j))
print(max_area)


