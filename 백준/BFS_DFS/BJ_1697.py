#백준 1697 숨바꼭질
from collections import deque
#입력
n, k = map(int, input().split())

vector = [-1, 1, 0]
que = deque([(n,0)])

while que:
    node = que.popleft()
    if node[0] == k : break
    vector[-1] = node[0]
    for i in range(3):
        newnode = (node[0]+vector[i], node[1]+1)
        if newnode[0] <=100000:
            que.append(newnode)
print(node[1])