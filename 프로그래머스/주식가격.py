def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        if stack == [] or prices[i] >= stack[-1][0]:
            stack.append((prices[i], i))
        else:
            last = stack.pop()
            answer[last[1]] = 1
            while stack:
                if stack[-1][0] <= prices[i] : break
                top = stack.pop()
                if top[0] > prices[i]:
                    answer[top[1]] = i - top[1]
                else:
                    answer[top[1]] = last[1] - top[1]
            stack.append((prices[i], i))

    while stack:
        top = stack.pop()
        answer[top[1]] = len(prices) - 1 - top[1]
    return answer

arr = [1,2,3,2,3]
print(solution(arr))