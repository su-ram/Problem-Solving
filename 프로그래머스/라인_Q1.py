from collections import deque
def solution(student, k):
    ones = [i for i in range(len(student)) if student[i] == 1]
    cnt = 0
    que = deque(ones)
    start = -1
    length = len(student)
    while len(que) >= k:
        s = que[0]
        e = que[k-1]
        left = s - start
        right = que[k] - e if len(que) > k else length - e
        cnt += left * right
        start = que.popleft()

    return cnt


s = [0,1,0,0,1,1,0,0,1,0,1,0,1,1,0]
k = 3
print(solution(s,k))