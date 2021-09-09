
dice = {
    'top' : 0,
    'bottom' : 0,
    'front' : 0,
    'rear' : 0,
    'left' : 0,
    'right' : 0
}


def move_dice(direction):
    dx = [0,0,0,-1,1]
    dy = [0,1,-1,0,0]
    global x,y, N, M
    nx, ny = x + dx[direction], y+dy[direction]

    if 0 <= nx < N and 0 <= ny < M :
        x, y = nx, ny
        return True
    return False


def roll_dice(direction):

    if direction == 1: #동
        temp = dice.get('top')
        dice['top'] = dice['left']
        dice['left'] = dice['bottom']
        dice['bottom'] = dice['right']
        dice['right'] = temp
        pass

    if direction == 2: #서
        temp = dice.get('top')
        dice['top'] = dice['right']
        dice['right'] = dice['bottom']
        dice['bottom'] = dice['left']
        dice['left'] = temp
        pass

    if direction == 3: #북
        temp = dice.get('top')
        dice['top'] = dice['front']
        dice['front'] = dice['bottom']
        dice['bottom'] = dice['rear']
        dice['rear'] = temp

    if direction == 4: #남
        temp = dice.get('rear')
        dice['rear'] = dice['bottom']
        dice['bottom'] = dice['front']
        dice['front'] = dice['top']
        dice['top'] = temp

    global x, y
    if maps[x][y] == 0 :
        maps[x][y] = dice.get('bottom')
    else:
        dice['bottom'] = maps[x][y]
        maps[x][y] = 0



N, M, x, y, K = map(int, input().split())
maps = [ list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

for cmd in commands:
    if move_dice(cmd):
        roll_dice(cmd)
        print(dice.get('top'))
