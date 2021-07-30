N = int(input())

origin = [list(map(int, input().split())) for _ in range(N)]
direction = ['U','D','L','R']
from copy import deepcopy

import math
max_num = -math.inf

def swipe(order, board):

    if order == 'L':
        for i in range(N):
            new_row = cal_row(board[i])
            board[i] = new_row


    elif order == 'R':
        for i in range(N):
            row = []
            for j in range(N-1, -1, -1):
                row.append(board[i][j])
            new_row = cal_row(row)
            board[i] = new_row[::-1]


    elif order == 'U':

        for i in range(N):
            row = []
            for j in range(N):
                row.append(board[j][i])
            new_row = cal_row(row)
            for j in range(N):
                board[j][i] = new_row[j]

    elif order == 'D':

        for i in range(N):
            row = []
            for j in range(N-1, -1, -1):
                row.append(board[j][i])
            new_row = cal_row(row)
            new_row = new_row[::-1]
            for j in range(N):
                board[j][i] = new_row[j]
    return board


def cal_row(row):
    global max_num

    while row.count(0) :
        row.remove(0)

    for i in range(len(row)):
        if i > 0 and row[i-1] == row[i] :
            row[i-1] *= 2
            row[i] =0

    for _ in range(N-len(row)):
        row.append(0)
    max_num = max(max_num, max(row))
    print(row)
    return row

def make_orders(arr):

    if len(arr) == 5 :
        board = deepcopy(origin)
        print()
        for o in arr:
            swipe(o, board)

        return

    for d in direction:
        arr.append(d)
        make_orders(arr)
        del arr[-1]

arr =[]
make_orders(arr)
print(max_num)
