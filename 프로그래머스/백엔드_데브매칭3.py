from collections import deque


def pop_candy(start, board, totalvisit):
    color = board[start[0]][start[1]]
    q = deque([start])
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = set([start])

    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 1<=nx<=6 and 1<=ny<=6 and board[nx][ny] == color and (nx,ny) not in visited:
                q.append((nx,ny))
                visited.add((nx,ny))

    if len(visited) >=3 :
        for x, y in visited:
            board[x][y] = 0

        for i in range(1, 7):
            m = []
            for j in range(6, 0, -1):
                if board[j][i] > 0:
                    m.append(board[j][i])
            for j in range(len(m)):
                board[6-j][i] = m[j]
            for j in range(6-len(m),0, -1):
                board[j][i] = 0

        return True
    return False





def search_same(board):
    visited = set()

    for i in range(6, 0, -1):
        for j in range(1, 7):
            if board[i][j] > 0 and (i,j) not in visited:
                while pop_candy((i, j), board, visited):
                    pass





def solution(macaron):
    board = [[0]*7 for _ in range(7)]

    for num, color in macaron:

        for i in range(6, 0, -1):
            if board[i][num] == 0:
                board[i][num] = color
                break
        search_same(board)
        for row in board[1:]:
            print(row[1:])
        print()



'''


0
1
1
1
0
0


'''



macaron = [[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]
print(solution(macaron))