n = int(input())
num = 1
for i in range(1, n+1):
    num *= i
cnt = 0
num = str(num)
num = list(num)

for i in num[::-1]:
    if i == '0' :
        cnt += 1
    else:
        break
print(cnt)