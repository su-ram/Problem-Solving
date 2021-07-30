
from collections import deque

def move(swipe, matrix):

    direction = swipe[0]
    r1, c1, r2, c2 = swipe[1:]
    total = 0
    print(swipe)
    if direction == 1 :

        for i in range(c1-1, c2):
            row = []
            for j in range(r1-1, r2):
                row.append(matrix[j][i])
            que = deque(row)
            total += (que[-1])
            que.appendleft(que.pop())

            for j in range(r1-1, r2):
                matrix[j][i] = que.popleft()

    elif direction == 2:

        for i in range(c1-1, c2):
            row = []
            for j in range(r1-1, r2):
                row.append(matrix[j][i])
            que = deque(row)
            total += que[0]
            que.append(que.popleft())
            for j in range(r1-1, r2):
                matrix[j][i] = que.pop()
        pass
    elif direction == 3:

        for i in range(r1-1, r2):
            row = []
            for j in range(c1-1, c2):
                row.append(matrix[i][j])

            que = deque(row)
            total += que[-1]
            que.appendleft(que.pop())

            for j in range(c1-1, c2):
                matrix[i][j] = que.popleft()


        pass
    elif direction == 4:

        for i in range(r1-1, r2):
            row = []
            for j in range(c1-1, c2):
                row.append(matrix[i][j])
            que = deque(row)
            total += que[0]
            que.append(que.popleft())

            for j in range(c1-1, c2):
                matrix[i][j] = que.popleft()

    for r in matrix:
        print(r)

    print()
    return total


def solution(rows, columns, swipes):
    answer = []
    sums = []
    for i in range(rows):
        arr = list(range(columns))
        arr = list(map(lambda x : i * columns + x + 1 , arr))
        answer.append(arr)
    for s in swipes:
        sums.append(move(s, answer))

    print(sums)



solution(4,3,[[1,1,2,4,3], [3,2,1,2,3], [4,1,1,4,3], [2,2,1,3,3]])
