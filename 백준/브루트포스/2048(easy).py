
N= int(input())
blocks = [ list(map(int, input().split())) for _ in range(N)]
direction = ['U', 'D', 'L', 'R']
import math, copy
result = -math.inf

'''
상하좌우로 미는 함수 4개를 정의하여 for문에서 모두 호출. 
미는 함수는 merged라는 새로운 리스트에 0이 아닌 수를 하나씩 append해가면서 
이전의 수가 중복된 수이면 *2하는 방식. 
마지막에는 개수차이만큼 0을 덧붙여서 blocks 갱신. 
'''

def left(blocks):
    global result

    for i in range(N):
        merged = []
        num = False
        for j in range(N):
            if blocks[i][j] == 0: continue
            if blocks[i][j] != 0 and num is False:
                merged.append(blocks[i][j])
                num = blocks[i][j]
                continue
            if num is not False and blocks[i][j] == num:
                merged[-1] *= 2
                num = False
                continue
            elif num is not False and blocks[i][j] != num:
                num = blocks[i][j]
                merged.append(blocks[i][j])

        merged += [0] * (N-len(merged))
        result = max(result, max(merged))

        for j in range(N):
            blocks[i][j] = merged[j]
    return blocks


def right(blocks):
    global result

    for i in range(N):
        merged = []
        num = False
        for j in range(N-1, -1, -1):
            if blocks[i][j] == 0: continue
            if blocks[i][j] != 0 and num is False:
                merged.append(blocks[i][j])
                num = blocks[i][j]
                continue
            if num is not False and blocks[i][j] == num:
                merged[-1] *= 2
                num = False
                continue
            elif num is not False and blocks[i][j] != num:
                num = blocks[i][j]
                merged.append(blocks[i][j])
        merged += [0] * (N - len(merged))
        result = max(result, max(merged))

        for j in range(N):
            blocks[i][j] = merged[N-1-j]
    return blocks


def up(blocks):
    global result

    for i in range(N):
        merged = []
        num = False
        for j in range(N):
            if blocks[j][i] == 0: continue
            if blocks[j][i] != 0 and num is False:
                merged.append(blocks[j][i])
                num = blocks[j][i]
                continue
            if num is not False and blocks[j][i] == num:
                merged[-1] *= 2
                num = False
                continue
            elif num is not False and blocks[j][i] != num:
                num = blocks[j][i]
                merged.append(blocks[j][i])
        merged += [0] * (N-len(merged))
        result = max(result, max(merged))

        for j in range(N):
            blocks[j][i] = merged[j]

    return blocks


def down(blocks):
    global result

    for i in range(N):
        merged = []
        num = False
        for j in range(N-1, -1, -1):
            if blocks[j][i] == 0: continue
            if blocks[j][i] != 0 and num is False:
                merged.append(blocks[j][i])
                num = blocks[j][i]
                continue
            if num is not False and blocks[j][i] == num:
                merged[-1] *= 2
                num = False
                continue
            elif num is not False and blocks[j][i] != num:
                num = blocks[j][i]
                merged.append(blocks[j][i])
        merged += [0] * (N - len(merged))
        result = max(result, max(merged))

        for j in range(N):
            blocks[j][i] = merged[N-1-j]
    return blocks


def next(cnt, blocks):

    if cnt == 6:return # 5번 이동했을 경우 멈춤.

    for i in range(4):

        #현재 블록 기준으로 4개 방향으로 이동하여 재귀적 탐색.

        if direction[i] == 'U':
            new_blocks = up(copy.deepcopy(blocks))
        if direction[i] == 'D':
            new_blocks = down(copy.deepcopy(blocks))
        if direction[i] == 'L':
            new_blocks = left(copy.deepcopy(blocks))
        if direction[i] == 'R':
            new_blocks = right(copy.deepcopy(blocks))

        next(cnt + 1, new_blocks)

next(0, blocks)

print(result)