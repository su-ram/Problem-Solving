n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
a, b = 0, 0

arr = []

while a < n and b < m:
    if A[a] <= B[b]:
        arr.append(A[a])
        a += 1
    elif A[a] >= B[b]:
        arr.append(B[b])
        b += 1


while b < m :
    arr.append(B[b])
    b+=1

while a < n:
    arr.append(A[a])
    a += 1

print(' '.join(map(str, arr)))