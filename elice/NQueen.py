import sys
sys.setrecursionlimit(100000)

def nQueen(position, n) :
    global cnt
    if len(position) == n:

        cnt += 1
        return 0

    candidate = list(range(n))

    for i in range(len(position)):

        if position[i] in candidate:
            candidate.remove(position[i])

        distance = len(position) - i

        if position[i] + distance in candidate:
            candidate.remove(position[i]+distance)

        if position[i] - distance in candidate:
            candidate.remove(position[i] - distance)

    if len(candidate) != 0:
        for c in candidate:
            position.append(c)
            nQueen(position,n)

    else:
        return cnt


n = int(input())
cnt = 0
for i in range(n):
    nQueen([i], n)

print(cnt)
