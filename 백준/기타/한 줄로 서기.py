N = int(input())
left = list(map(int, input().split()))
ordered = []
for i in range(N-1, -1, -1):
    ordered.insert(left[i], i+1)
print(' '.join(list(map(str, ordered))))

