N = int(input())

nodes = []
for i in input().rstrip().split():
    if i.startswith('-'):
        nodes.append(-int(i[1:]))
    else:
        nodes.append(int(i))

remove = int(input())

# 누가 누구를 원하는지 나타내는 그래프 표현
graph = [[] for _ in range(N + 1)]
for i in range(N):
    parent = nodes[i]
    if parent == -1:
        parent = N
    graph[parent].append(i)

rootnode = graph[-1][0]

def Solution(n):
    nodes[n] = -2
    child = graph[n]
    if child == []:
        return
    else:
        for i in child:
            Solution(i)
def findLeaf(n):

    child = graph[n]

    if child==[]:
        return [n]

    total = []

    for i in child:
        total.extend(findLeaf(i))

    return total

leaves=findLeaf(rootnode)
Solution(remove)
afterRemove = []
for i in leaves:
    if nodes[i] != -2:
        afterRemove.append(i)


print(len(afterRemove))

