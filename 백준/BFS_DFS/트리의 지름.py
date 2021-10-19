import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    p, c, d = map(int, input().split())
    graph[p].append((c,d))
    graph[c].append((p,d))


def dfs(start, visited):
    for n in nodes[start]:
        if visited[n[0]] == -1:
            visited[n[0]] = visited[start] + n[1]
            dfs(n[0], visited)


def solution(n, graph):

    global nodes
    nodes = graph
    visited = [-1] * (n+1)
    visited[1] = 0
    dfs(1, visited)
    maxnum = max(visited)
    maxindex = visited.index(maxnum)

    visited = [-1] * (n+1)
    visited[maxindex] = 0
    dfs(maxindex, visited)


    return max(visited)





print(solution(n, graph))
