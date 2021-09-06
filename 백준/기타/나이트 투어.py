pos = input()
x, y = ord(pos[0]) - ord('A'), 6 - int(pos[1])
start = (x,y)
result = 'Valid'
visited = [[False]*6 for _ in range(6)]
visited[x][y] = True

def move(source, target):
    dx, dy = abs(source[0] - target[0]), abs(source[1] - target[1])
    if dx == 0 or dy == 0 :
        return False
    if dx + dy != 3 :
        return False
    return True

for _ in range(35):
    pos = input()
    i,j = ord(pos[0]) - ord('A'), 6 - int(pos[1])
    if move((x,y),(i,j)) is False :
        result = 'Invalid'
    if visited[i][j] is True:
        result = 'Invalid'
    x, y = i, j
    visited[i][j] = True

if move(start, (i,j)) is False:
    result = 'Invalid'

for row in visited:
    if False in row :
        result = 'Invalid'
        break
print(result)

