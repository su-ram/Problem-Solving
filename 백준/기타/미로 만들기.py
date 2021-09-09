n = int(input())
maze = [['1']*101 for _ in range(101)]
cmds = input()
# 2
#1 3
# 0
direction = 0
dx = [1,0,-1,0]
dy = [0,-1,0,1]
i,j = 50, 50
maze[i][j] = '.'
h = [0,0] #up, down
w = [0,0] #left, right


def turnright():
    global direction
    direction += 1
    if direction > 3 : direction = 0


def turnleft():
    global direction
    direction -=  1
    if direction < 0 : direction = 3


def changesize():
    if i - 50 > 0 : #down
        h[1] = max(h[1], abs(i-50))
    if i - 50 < 0 : #up
        h[0] = max(h[0], abs(i-50))
    if j - 50 > 0 : #right
        w[1] = max(w[1], j-50)
    if j - 50 < 0 : #left
        w[0] = max(w[0], abs(j-50))


for cmd in cmds:
    if cmd == 'F':
        i += dx[direction]
        j += dy[direction]
        maze[i][j] = '.'
        changesize()
    elif cmd == 'R':
        turnright()
    elif cmd == 'L':
        turnleft()

height = sum(h) + 1
width = sum(w) + 1
start = (50-h[0], 50-w[0])

for x in range(height):
    row = (maze[start[0]+x][start[1]:start[1]+width])
    row = ''.join(row).replace('1','#')
    print(row)

