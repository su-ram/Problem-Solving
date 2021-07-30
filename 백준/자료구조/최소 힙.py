import heapq, sys
input = sys.stdin.readline
N = int(input().rstrip())
heap = []

for _ in range(N):
    num = int(input().rstrip())
    if num == 0 :
        print(heapq.heappop(heap) if heap != [] else 0)
    else:
        heapq.heappush(heap, num)