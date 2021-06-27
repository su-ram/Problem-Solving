N = int(input())
times = list(map(int, input().split())).sort()
total = 0
for i in range(N):
    total += times[i]*(N-i)
print(total)