N = int(input())
prev = 0
next = 0
for i in range(N):
    add = prev + 1
    now = next + add
    next= now + add
    prev = now
print((next+1)%9901)


