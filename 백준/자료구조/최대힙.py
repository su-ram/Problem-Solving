import heapq, sys
input = sys.stdin.readline
N = int(input().rstrip())
heap = []
for _ in range(N):
    num = int(input())
    if num == 0 :
        print(0 if heap == [] else -heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)