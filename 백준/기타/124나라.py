def solution(n):
    c = ['1', '2', '4']
    cnt = 0
    num = 1
    prev = 0
    while True:
        num *= 3
        if prev >= n: break
        prev += num
        cnt += 1
    length = cnt
    gap = n - prev - 1
    ans = ''

    for i in range(length - 1, 0, -1):
        num = 3 ** i
        now = gap // num
        now = now % (3)
        ans += c[now]

    ans += c[gap % 3]

    return ans

for i in range(1, 50):
    print(i, solution(i))