n, m = map(int, input().split())
truth = list(map(int,input().split()))
party = [ list(map(int, input().split())) for _ in range(m)]
from collections import defaultdict, deque


def solution(n, m, truth, party):

    connect = defaultdict(list)
    knowing = set()

    if len(truth) > 0:
        for i in range(len(truth)-1):
            connect[truth[i]].append(truth[i+1])
            connect[truth[i+1]].append(truth[i])

        for p in party:
            p = p[1:]
            if len(p) > 1:
                for i in range(len(p)-1):
                    connect[p[i]].append(p[i+1])
                    
        first = truth[0]
        q = deque([first])
        knowing.add(first)
        while q:
            x = q.popleft()
            for near in connect.get(x):
                if near not in knowing:
                    q.append(near)
                    knowing.add(near)

    knowing = list(knowing)
    knowing.sort()
    cnt = 0
    for p in party:
        cnt += 1
        for x in p[1:]:
            if x in knowing:
                cnt -= 1
                break

    return cnt




print(solution(n,m, truth[1:], party))