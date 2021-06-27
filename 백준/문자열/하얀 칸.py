
chess = [list(input()) for _ in range(8)]
cnt = 0
is_white = True
for i in range(8):

    is_white = not is_white

    for j in range(is_white, 8, 2):
        if chess[i][j] == 'F':
            cnt += 1

print(cnt)
