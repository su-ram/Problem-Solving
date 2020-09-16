from collections import deque
n=int(input())
m=int(input())
connect = {}
for i in range(m):
    c1, c2 = map(int, input().split())
    if c1 not in connect.keys():
        connect[c1] = [c2]
    else:
        connect[c1]+=[c2]
    if c2 not in connect.keys():
        connect[c2] = [c1]
    else:
        connect[c2]+=[c1]
    

visited=[]
que = deque()
que.append(1)
num = 0 

while que:
    node = que.popleft()
    visited.append(node)
    if node in connect.keys():
        temp=connect[node]
        for i in temp:
            if i not in visited and i not in que:
                que.append(i)
print(len(visited)-1)
