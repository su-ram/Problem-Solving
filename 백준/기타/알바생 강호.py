n = int(input())
tips = [ int(input()) for _ in range(n)]
tips.sort(reverse=True)
total = 0
for tip in zip(tips, range(n)):
    if tip[0] - tip[1] > 0 :
        total += tip[0] - tip[1]
print(total)