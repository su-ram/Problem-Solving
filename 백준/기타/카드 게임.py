from collections import Counter

cards = [ tuple(input().split()) for _ in range(5)]


def solution(cards):

    color = []
    num = []
    serial = True
    point = -1

    for c in cards:
        color.append(c[0])
        num.append(int(c[1]))
    num.sort()
    prev = num[0] - 1

    for n in num:
        if n != prev + 1:
            serial = False
            break
        prev = n

    colorcnt = list(Counter(color).most_common())
    numcnt = list(Counter(num).most_common())
    getpoint = False

    if len(colorcnt) == 1 and serial:
        point = max(point, num[-1] + 900)
        getpoint = True

    if len(numcnt) == 2:
        if numcnt[0][1] == 4:
            point = max(point, numcnt[0][0] + 800)
            getpoint = True
        if numcnt[0][1] == 3:
            point = max(point, numcnt[0][0]*10 + numcnt[1][0]+700)
            getpoint = True

    if len(colorcnt) == 1:
        point = max(point, num[-1] + 600)
        getpoint = True

    if serial:
        point = max(point, num[-1] + 500)
        getpoint = True

    if numcnt[0][1] == 3:
        point = max(point, numcnt[0][0] + 400)
        getpoint = True

    if numcnt[0][1] == numcnt[1][1] == 2:
        m = max(numcnt[0][0], numcnt[1][0])
        n = min(numcnt[0][0], numcnt[1][0])
        point = max(point, m*10 + n + 300)
        getpoint = True

    for n, c in numcnt:
        if c == 2:
            point = max(point, n + 200)
            getpoint = True

    if not getpoint:
        point = max(point, num[-1] + 100)


    return point


print(solution(cards))


