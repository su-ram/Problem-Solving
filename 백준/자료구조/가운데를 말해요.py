import sys, heapq
input = sys.stdin.readline
N = int(input())
minh, maxh = [], []
for i in range(N):
    num = int(input())

    if len(maxh) == len(minh):
        heapq.heappush(minh, -num)
    else:
        heapq.heappush(maxh, num)

    if len(maxh) >0 and len(minh) > 0 and -minh[0] > maxh[0]:
        temp = -(heapq.heappop(minh))
        heapq.heappush(minh, -heapq.heappop(maxh))
        heapq.heappush(maxh, temp)
    print(-minh[0])

