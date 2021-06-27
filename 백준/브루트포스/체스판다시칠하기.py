'''
체스판의 좌상단을 가능한 범위만큼 순회한다. N - 8 , M - 8 만큼.
체스판의 좌상단 값을 기준값으로 놓고 두 가지 경우의 수를 구한다.
- Black  / White
value는 B/W인지를 나타내고 다음 줄로 넘어갈 때 마다 서로 반대되므로
not 연산을 한다.
'''


N, M = map(int, input().split())
board = [0] * N

for i in range(N):
    board[i] = list(input())

chess = {
    'B' : True,
    'W' : False
}

def check_value(x, y, value):

    cnt = 0
    for i in range(x, x+8):
        value = not value
        for j in range(y, y+8, 2):
            if chess.get(board[i][j]) != value:
                cnt += 1

        for j in range(y+1, y+9, 2):
            if chess.get(board[i][j]) == value:
                cnt +=1

    return cnt

repainting = M * N

for i in range(N-7):
    for j in range(M-7):
        start = chess.get(board[i][j])
        cnt = check_value(i,j,not start)
        cnt2 = check_value(i,j, start)
        repainting = min(cnt, cnt2, repainting)

print(repainting)
