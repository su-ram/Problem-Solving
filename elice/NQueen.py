
def nQueen(q,n):

    global cnt

    if len(q) == n :
        cnt += 1
        return 0

    candidate = []
    x1 = len(q)

    for i in range(n):

        y1 = i

        if i in q :
            continue

        promising = True
        #기울기의 절댓값이 1
        for x2, y2 in enumerate(q):

            # 기존 퀸의 좌표 : x, y
            if abs((y2-y1)/(x2-x1)) == 1 :
                promising = False
                break

        if not promising :
            continue

        candidate.append(i)

    for c in candidate:
        nQueen(q + [c], n)


n = int(input())
cnt = 0
for i in range(n):
    nQueen([i], n)

print(cnt)

