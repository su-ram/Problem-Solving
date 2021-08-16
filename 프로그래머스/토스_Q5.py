from collections import deque
def solution(fruitWeights, k):
    answer = []
    window = fruitWeights[:k]
    window = deque(window)
    max_num = set([max(window)])
    for i in range(k, len(fruitWeights)):
        window.popleft()
        window.append(fruitWeights[i])
        max_num.add(max(window))
    return sorted(max_num, reverse=True)
print(solution([30, 40, 10, 20, 30], 3))