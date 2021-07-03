N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
origin = board.copy()
direction = ['U','D','L','R']
from itertools import product
orders = product(direction, repeat=5)

def swipe(order):
    print(order)
    if order in ['L', 'R']:

        for i in range(N):
            curr = -1

            for j in range(N):
                if not board[i][j]:
                    continue
                if curr == -1:
                    curr = j
                elif board[i][curr] == board[i][j]:
                    board[i][curr] *= 2
                    curr = -1
                    board[i][j] = 0
                elif board[i][curr] != board[i][j]:
                    curr = j

            while board[i].count(0):
                board[i].remove(0)

            if order == 'L':
                while N - len(board[i]):
                    board[i].append(0)
            else:
                while N - len(board[i]):
                    board[i].insert(0,0)
            print(board[i])

    else:
        for i in range(N):
            row = []
            for j in range(N):
                row.append(board[j][i])
            curr = -1
            for j in range(N):
                if not row[j]:
                    continue
                if curr == -1:
                    curr = j
                elif row[curr] == row[j]:
                    row[curr] *= 2
                    curr = -1
                    row[j] = 0
                elif row[curr] != row[j]:
                    curr = j

            while row.count(0):
                row.remove(0)

            if order == 'U':
                while N - len(row):
                    row.append(0)
            else:
                while N - len(row):
                    row.insert(0,0)

            for j in range(N):
                board[j][i] = row[j]

import math,copy
max_num = -math.inf
for order in orders:

    board = copy.deepcopy(origin)

    for o in order:
        swipe(o)
        for row in board:

            max_num = max(max(row), max_num)
print(max_num)
