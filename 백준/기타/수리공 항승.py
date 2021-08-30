n, l = map(int,input().split())
positions = list(map(int, input().split()))
index = 0
cnt = 0
positions.sort()
while index < n :
    end = positions[index] + l
    adds = 0
    for i in range(l):
        if i + index >= n : break
        if positions[i+index] < end :
            adds += 1
            continue
        else:
            break
    cnt += 1
    index += adds
print(cnt)