import heapq

def solution(food_times, k):

    length = len(food_times)
    if sum(food_times) <= k:
        return -1

    que = []
    for i in range(length):
        heapq.heappush(que, (food_times[i], i+1))

    sum_times = 0
    prev = 0

    while sum_times + (que[0][0]-prev) * length <= k :
        now = heapq.heappop(que)[0]
        sum_times += (now-prev) * length
        length -= 1
        prev = now

    que = sorted(que, key=lambda x : x[1])
    return que[(k-sum_times) % length][1]


food_times = [3,1,2]
k = 5
print(solution(food_times,k))