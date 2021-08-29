n = int(input())
furious = list(map(int,input().split()))
furious.sort()
start = 0
groups = 0
while start < n:
    start += furious[start]
    groups += 1
print(groups)
