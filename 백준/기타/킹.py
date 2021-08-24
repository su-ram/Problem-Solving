king, rock, n = input().split()
king = (int(king[1]) - 1, ord(king[0]) - ord('A'))
rock = (int(rock[1]) - 1 , ord(rock[0]) - ord('A'))
direction = {
    'R' : (0,1),
    'L' : (0,-1),
    'B' : (-1, 0),
    'T' : (1, 0),
    'RT' : (1, 1),
    'LT' : (1, -1),
    'RB' : (-1, 1),
    'LB' : (-1, -1)
}


def isinrange(pos):
    return True if 0 <= pos[0] < 8 and 0 <= pos[1] < 8 else False


def move(order) :
    nx, ny = direction.get(order)
    global rock, king
    king = (king[0] + nx, king[1] + ny)
    if not isinrange(king):
        king = (king[0] - nx, king[1] - ny)
        return
    if king == rock :
        rock = (rock[0] + nx, rock[1] + ny)
        if not isinrange(rock):
            king = (king[0] - nx, king[1] - ny)
            rock = (rock[0] - nx, rock[1] - ny)


for _ in range(int(n)):
    move(input())

king = chr(65+int(king[1])) + str(int(king[0]) + 1)
rock = chr(65+int(rock[1])) + str(int(rock[0]) + 1)
print(king)
print(rock)

