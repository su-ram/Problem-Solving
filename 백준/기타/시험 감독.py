N = int(input())
a = list(map(int, input().split()))
B, C = map(int, input().split())
result = N
a = list(map(lambda x : x - B, a))
a = [divmod(n, C) for n in a if n > 0]
for n in a :
    if n[0] > 0 :
        result += n[0]
    if n[1] > 0 :
        result += 1
print(result)