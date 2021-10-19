N = int(input())
M = int(input())
ids= list(map(int, input().split()))
import heapq

def solution(N, M, ids):
    que = []
    for t, id in enumerate(ids):
        duplicate = False
        for j in range(len(que)):
            if que[j][-1] == id:
                que[j][0] += 1
                duplicate = True
                break
        if not duplicate:
            if len(que) < N :
                que.append([1, t, id])
            else:
                heapq.heapify(que)
                heapq.heappop(que)
                que.append([1,t,id])

    que = list(map(lambda x : x[-1], que))
    que.sort()

    for n in que:
        print(n, end=' ')


solution(N, M, ids)