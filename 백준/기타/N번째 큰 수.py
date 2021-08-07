import heapq
n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for i in range(n-1):
    arr = list(map(int, input().split()))
    for j in arr :
        heapq.heappush(heap, j)
        heapq.heappop(heap)

print(heapq.heappop(heap))