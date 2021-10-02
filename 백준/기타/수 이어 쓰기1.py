n = input()
length = len(n)
cnt = 0
result  = 0
for i in range(length-1):
    cnt += 10 ** (i) * 9
    result += (10 ** (i) * 9) * (i+1)
cnt = length * (int(n) - cnt)
result += cnt
print(result)