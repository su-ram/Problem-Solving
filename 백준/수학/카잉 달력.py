

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    result = -1
    num = y
    while num <= M*N:
        if num % M == x % M :
            result = num
            break
        num += N
    print(result)