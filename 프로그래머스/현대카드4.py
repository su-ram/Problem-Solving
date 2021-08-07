road = list(input())
road = list(map(int, road))
n = int(input())
start, end = 0, 0
repair = [-1]

for i in range(len(road)):
    if road[i] == 0:
        if len(repair) == n+1:
            repair.pop(0)
        repair.append(i)

    l1 = end - start
    l2 = i+1 - repair[0]

    if l2 > l1 :
        start = repair[0] + 1
        end = i + 1

print(end-start)

