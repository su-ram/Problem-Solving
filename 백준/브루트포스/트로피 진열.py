n = int(input())
arr = [int(input()) for _ in range(n)]

def solution(arr):
    stack = []
    cnt = 0
    for n in arr:
        if stack == []:
            stack.append(n)
            cnt += 1

        elif stack[-1] < n :
            stack.append(n)
            cnt += 1
    return cnt

print(solution(arr))
print(solution(arr[::-1]))