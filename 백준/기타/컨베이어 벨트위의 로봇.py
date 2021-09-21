N, K = map(int, input().split())
a = list(map(int, input().split()))
robot = [0] * (N)
from collections import deque
robot = deque(robot)
conveyor = deque(a)
result = 1
while True :

    #1
    robot.rotate(1)
    conveyor.rotate(1)
    robot[-1] = 0

    #2
    for i in range(N-2, -1, -1):
        if conveyor[i+1] > 0 and robot[i+1] == 0 and robot[i] == 1:
            robot[i] = 0
            robot[i+1] = 1
            conveyor[i+1] -= 1
    robot[-1] = 0

    #3
    if robot[0] == 0 and conveyor[0] > 0 :
        robot[0] = 1
        conveyor[0] -= 1

    if conveyor.count(0) >= K :
        print(result)
        break

    result += 1