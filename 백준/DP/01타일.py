N = int(input())
if N > 2:
    a, b = 1, 2
    num = 0
    for i in range(3, N+1):
        num = (a + b) % 15746
        temp = b
        b = num % 15746
        a = temp % 15746

else:
    num = N
print(num)