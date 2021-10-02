R, C, T = map(int, input().split())
cleaner = []
adds = dict()
room = []
for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        adds[(i,j)] = []
    if -1 in row:
        cleaner.append((i,row.index(-1)))
    room.append(row)


def spread():

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                cnt = 0
                add = room[i][j] // 5
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        adds.get((nx,ny)).append(add)
                        cnt += 1
                adds.get((i,j)).append(-(add*cnt))
    for k, v in adds.items():
        x, y = k
        total = sum(v)
        room[x][y] += total
        adds[k] = []


def blow():
    tx, ty = cleaner[0]
    bx, by = cleaner[1]

    #top
    # right
    rightbottom = room[tx][-1]
    prev = 0
    for j in range(1, C):
        temp = room[tx][j]
        room[tx][j] = prev
        prev = temp

    # up
    righttop = room[0][-1]
    prev = rightbottom
    for i in range(tx-1, -1, -1):
        temp = room[i][-1]
        room[i][-1] = prev
        prev = temp

    #left
    lefttop = room[0][0]
    prev = righttop
    for j in range(C-2, -1, -1):
        temp = room[0][j]
        room[0][j] = prev
        prev = temp

    #down
    prev = lefttop
    for i in range(1, tx):
        temp = room[i][0]
        room[i][0] = prev
        prev = temp

    room[tx][ty] = -1


    #bottom
    #right
    righttop = room[bx][-1]
    prev = 0
    for j in range(1, C):
        temp = room[bx][j]
        room[bx][j] = prev
        prev = temp

    #down
    rightbottom = room[-1][-1]
    prev = righttop
    for i in range(bx+1,R):
        temp = room[i][-1]
        room[i][-1] = prev
        prev = temp

    #left
    leftbottom = room[-1][0]
    prev = rightbottom
    for j in range(C-2,-1,-1):
        temp = room[-1][j]
        room[-1][j] = prev
        prev = temp

    #up
    prev = leftbottom
    for i in range(R-2,tx,-1):
        temp =room[i][0]
        room[i][0] = prev
        prev = temp
    room[bx][by] = -1


def howmany():
    result = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0 :
                result += room[i][j]
    return result


for _ in range(T):
    spread()
    blow()

print(howmany())


