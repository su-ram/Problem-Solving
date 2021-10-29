R, C, M = map(int, input().split())
sharks = [ list(map(int, input().split())) for _ in range(M)]
'''
 1 위
 2 아래
 3 오른쪽
 4 왼쪽
'''

def move(board):

    visited = set()

    for i in range(1, r+1):
        for j in range(1, c+1):
            if board[i][j] != 0:

                x, y = i, j
                s,d,z = board[i][j]
                board[i][j] = 0
                for _ in range(s):

                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 1<=nx<=r and 1<=ny<=c:
                        x = nx
                        y = ny
                        continue

                    #2345
                    if d==2:
                        d = 1
                    elif d == 4:
                        d = 3
                    else:
                        d += 1
                    x = x + dx[d]
                    y = y + dy[d]

                visited.add((x,y,s,d,z))

    for shark in visited:

        x,y,s,d,z = shark
        if board[x][y] == 0 or board[x][y][-1] < z:
            board[x][y]= (s,d,z)




def solution(R,C,sharks):
    global r, c, dx, dy
    r,c = R, C
    board = [ [0] * (c+1) for _ in range(r+1)]
    answer = 0
    dx = [0, -1,1,0,0]
    dy = [0, 0,0,1,-1]

    for shark in sharks:
        x,y,s,d,z = shark
        board[x][y] = (s,d,z)

    for j in range(1, c+1):
        catch = 0
        for i in range(1, r+1):
            if board[i][j] != 0:
                catch = board[i][j]
                break
        if catch != 0:
            answer += catch[-1]
            board[i][j] = 0

        move(board)


    print(answer)






solution(R,C,sharks)