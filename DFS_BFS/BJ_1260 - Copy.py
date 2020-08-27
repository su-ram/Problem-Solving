import sys
from collections import deque
print("I'm the  copy one.")
print("I'm udated.!!")
nodes,edges,root=map(int,sys.stdin.readline().split())

g=[[]]
for _ in range(nodes):
    g.append([])

for _ in range(edges):
    i,j=map(int,sys.stdin.readline().split())
    g[i].append(j)
    g[j].append(i)

for i in g:
    i.sort()


def DFS(g,root):

    visited=[]
    stack=[root]

    while stack:

        node = stack.pop()
        sis=g[node]
        sis=reversed(sis)

        if node not in visited:
            visited.append(node)
            print(node,end=' ')
            stack.extend(sis)
    return visited
DFS(g,root)
print()
def BFS(g,root):

    visited=[]
    queue=deque([root])

    while queue:

        node = queue.popleft()
        sis=g[node]


        if node not in visited:
            visited.append(node)
            print(node,end=' ')
            queue.extend(sis)

    return visited
BFS(g,root)



