board = [ input().split() for _ in range(5)]
nums =set()
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def DFS(x,y,d,num):
    if d == 5 :
        nums.add(str(num))
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            DFS(nx,  ny, d+1, num + board[nx][ny])

for i in range(5):
    for j in range(5):
        DFS(i,j,0,board[i][j])


print(len(nums))