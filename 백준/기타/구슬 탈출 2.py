
from collections import deque


N, M = map(int, input().split())
board = []
beads = {'R':0, 'B':0}
result =[11,11]


for i in range(N):
    row = list(input())
    if 'R' in row:
        j = row.index('R')
        beads['R'] = (i,j)
    if 'B' in row:
        j = row.index('B')
        beads['B'] = (i,j)
    if 'O' in row:
        j = row.index('O')
        row[j] = '.'
        hole = (i,j)
    board.append(row)


visited = []
direction =['up','down', 'left', 'right']


def ishole(i,j):
    if (i,j) == hole:return True
    return False


def move(x,y, nd):
    nx, ny = x, y
    if nd == 'up':
        while board[nx-1][ny] == '.' and not ishole(nx,ny):
            nx -= 1

    if nd == 'down':
        while board[nx+1][ny] == '.' and not ishole(nx, ny):
            nx += 1

    if nd == 'left':
        while board[nx][ny-1] == '.' and not ishole(nx, ny):
            ny -= 1

    if nd == 'right':
        while board[nx][ny+1] == '.' and not ishole(nx, ny):
            ny += 1

    board[x][y] = '.'
    if not ishole(nx,ny):
        board[nx][ny] = '*'
    return (nx, ny)


def tilt(r,b,nd):

    if nd == 'up':
        if r[0] <= b[0]:
            nr = move(r[0], r[1], nd)
            nb = move(b[0], b[1], nd)
        else:
            nb = move(b[0], b[1], nd)
            nr = move(r[0], r[1], nd)

    if nd == 'down':
        if r[0] >= b[0]:
            nr = move(r[0], r[1], nd)
            nb = move(b[0], b[1], nd)
        else:
            nb = move(b[0], b[1], nd)
            nr = move(r[0], r[1], nd)

    if nd == 'left':
        if r[1] <= b[1]:
            nr = move(r[0], r[1], nd)
            nb = move(b[0], b[1], nd)
        else:
            nb = move(b[0], b[1], nd)
            nr = move(r[0], r[1], nd)

    if nd == 'right':
        if r[1] >= b[1]:
            nr = move(r[0], r[1], nd)
            nb = move(b[0], b[1], nd)
        else:
            nb = move(b[0], b[1], nd)
            nr = move(r[0], r[1], nd)

    board[nr[0]][nr[1]] = '.'
    board[nb[0]][nb[1]] = '.'

    board[r[0]][r[1]] = '*'
    board[b[0]][b[1]] = '*'

    if nr == r and nb == b:
        return False
    else:
        return nr, nb




def BFS():
    q = deque([(beads.get('R'), beads.get('B'), 1)])
    visited.append((beads.get('R'), beads.get('B')))
    global hole, result, board

    while q :
        r, b, c = q.popleft()

        if c > 10:
            break
        board[r[0]][r[1]] = '*'
        board[b[0]][b[1]] = '*'
        for i in range(4):
            nd = direction[i]
            next = tilt(r,b,nd)

            if next is False:
                continue

            if hole == next[0] and hole == next[1]:
                board[r[0]][r[1]] = '*'
                board[b[0]][b[1]] = '*'
                continue
            if hole == next[0]:
                result[0] = min(result[0], c)

            if hole == next[1] :
                result[1] = min(result[1], c)

            if (next[0], next[1]) not in visited:
                q.append((next[0], next[1], c+1))
                visited.append((next[0], next[1]))

        board[r[0]][r[1]] = '.'
        board[b[0]][b[1]] = '.'

BFS()
print(result[0] if result[0] != 11 else -1)
