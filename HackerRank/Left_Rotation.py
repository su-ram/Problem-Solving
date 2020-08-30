from collections import deque
nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
queue = deque(a)

for i in range(d):
    num = queue.popleft()
    queue.append(num)
for _ in a:
    print(queue.popleft(), end=' ')