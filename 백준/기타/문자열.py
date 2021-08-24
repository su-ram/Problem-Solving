a, b = input().split()

def diff(str1, str2) :
    cnt = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i] :
            cnt += 1
    return cnt


gap = len(b) - len(a)
result = len(b) + 1
for i in range(gap+1):
    result = min(result, diff(a, b[i:]))
print(result)