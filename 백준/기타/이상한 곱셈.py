n, m = list(input().split())
result = 0
for a in n :
    for b in m :
        result += int(a) * int(b)
print(result)