
dirs={
    1: [[(0)],[(1)],[(2)],[(3)]],
    2: [(0,2), (1,3)],
    3: [(0,1), (1,2), (2,3), (3,0)],
    4: [(0,1,2), (1,2,3), (2,3,0), (3,0,1)],
    5: [(0,1,2,3)]
}


def left(x,y):
    d = (0,-1)
    nx, ny = x, y

    while 0 <= ny < m and room[nx][ny] != 6:
        room[nx][ny] = '#'
        ny = ny + d[1]


def right(x,y):
    d = (0, 1)
    nx, ny = x, y

    while 0 <= ny < m and room[nx][ny] != 6:
        room[nx][ny] = '#'
        ny = ny + d[1]


def up(x,y):
    d = (-1, 0)
    nx, ny = x, y

    while 0 <= nx < n and room[nx][ny] != 6:
        room[nx][ny] = '#'
        nx = nx + d[0]

def down(x,y):
    d = (1, 0)
    nx, ny = x, y

    while 0 <= nx < n and room[nx][ny] != 6:
        room[nx][ny] = '#'
        nx = nx + d[0]


def watch(moves, cctv):

    length = len(moves)

    for i in range(length):
        x, y = cctv[i][0], cctv[i][1]

        for m in moves[i]:
            if m == 0: up(x, y)
            if m == 1: right(x, y)
            if m == 2: down(x, y)
            if m == 3: left(x, y )

    unseen = 0
    for row in room:
        unseen += row.count(0)

    return unseen


n, m = map(int, input().split())
room = []
cctv = []

for i in range(n):
    row = list(map(int, input().split()))
    room.append(row)
    for j in range(m):
        if 0 < row[j] < 6 :
            cctv.append((i,j))


def DFS(arr, d, cctv, cnt):
    if d == cnt:
        global moves
        moves.append(arr)
        return
    now = cctv[d]
    now = room[now[0]][now[1]]
    for i in dirs.get(now):
        DFS(arr+[i], d+1, cctv, cnt)


import copy
moves = []
origin = copy.deepcopy(room)
DFS([], 0, cctv, len(cctv))
result = n*m


for move in moves:
    room = copy.deepcopy(origin)
    cnt = watch(move, cctv)
    result = min(result, cnt)

print(result)