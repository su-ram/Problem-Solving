
from collections import deque

gear = [[]]
right = 2
left = 6


for _ in range(4):
    row = list(map(int, list(input())))
    row = deque(row)
    gear.append(row)


for _ in range(int(input())):
    index, dir = map(int, input().split())
    rotate = [0] * 5 #1 시계 -1 반시계 0 회전 안함

    if index == 1:
        rotate[1] = dir
        rotate[2] = -rotate[1] if gear[1][right] + gear[2][left] == 1 else 0
        rotate[3] = -rotate[2] if gear[2][right] + gear[3][left] == 1 else 0
        rotate[4] = -rotate[3] if gear[3][right] + gear[4][left] == 1 else 0
        pass
    elif index == 2:
        rotate[2] = dir
        rotate[1] = -rotate[2] if gear[1][right] + gear[2][left] == 1 else 0
        rotate[3] = -rotate[2] if gear[2][right] + gear[3][left] == 1 else 0
        rotate[4] = -rotate[3] if gear[3][right] + gear[4][left] == 1 else 0
        pass
    elif index == 3:
        rotate[3] = dir
        rotate[2] = -rotate[3] if gear[3][left] + gear[2][right] == 1 else 0
        rotate[1] = -rotate[2] if gear[2][left] + gear[1][right] == 1 else 0
        rotate[4] = -rotate[3] if gear[3][right] + gear[4][left] == 1 else 0
        pass
    elif index == 4:
        rotate[4] = dir
        rotate[3] = -rotate[4] if gear[3][right] + gear[4][left] == 1 else 0
        rotate[2] = -rotate[3] if gear[3][left] + gear[2][right] == 1 else 0
        rotate[1] = -rotate[2] if gear[2][left] + gear[1][right] == 1 else 0

    for i in range(1, 5):
        gear[i].rotate(rotate[i])

points = 0
for i in range(4):
    if gear[i+1][0]:
        points += 2 ** i
print(points)