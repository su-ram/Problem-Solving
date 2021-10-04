import math

n = int(input())
a = [ list(map(int, input().split())) for _ in range(n)]
d = []
for i in range(n):
    for j in range(n):
        d.append((i+1,j+1))


def boarders(start):

    top = start
    x, y = top
    points = []

    for d1, d2 in d:
        point = {'top':start}
        line = []
        right = (x + d2, y + d2)
        if 0 <= right[0] < n and 0 <= right[1] < n:
            point['right'] = right
            for i in range(d2):
                line.append((x+(1+i), y+(1+i)))
        else:
            continue

        down = (right[0] + d1, right[1] - d1)
        if 0 <= down[0] < n and 0 <= down[1] < n:
            point['down'] = down
            for i in range(d1):
                line.append((right[0]+(1+i), right[1]-(1+i)))
        else:
            continue

        left = (down[0] - d2, down[1] - d2)
        if 0 <= left[0] < n and 0 <= left[1] < n:
            point['left'] = left
            for i in range(d2):
                line.append((down[0]-(1+i), down[1]-(1+i)))
        else:
            continue

        for i in range(d1):
            line.append((left[0]-(1+i), left[1]+(1+i)))
        point['line'] = line
        points.append(point)
    return points


def area(points):

    global result


    for point in points:
        t = point.get('top')
        d = point.get('down')
        l = point.get('left')
        r = point.get('right')
        line = point.get('line')
        area = [0]*6

        for x in range(n):
            for y in range(n):

                if (x,y) in line:
                    area[5] += a[x][y]
                    continue
                #one
                gap = x - t[0]
                if 0 <= x < t[0] and 0 <= y <= t[1]:
                    area[1] += a[x][y]
                    continue
                elif t[0] <= x < l[0] and 0 <= y < t[1] - gap:
                    area[1] += a[x][y]
                    continue

                gap = x - l[0]
                if l[0] <= x <= d[0] and 0 <= y < l[1] + gap:
                    area[3] += a[x][y]
                    continue
                elif d[0] < x < n and 0 <= y < d[1]:
                    area[3] += a[x][y]
                    continue

                gap = x - t[0]
                if 0 <= x < t[0] and t[1] < y < n:
                    area[2] += a[x][y]
                    continue
                elif t[0] <= x <= r[0] and gap + t[1] < y < n:
                    area[2] += a[x][y]
                    continue

                gap = x - r[0]
                if r[0] < x <= d[0] and r[1] - gap < y < n:
                    area[4] += a[x][y]
                    continue
                elif d[0] < x < n and d[1] <= y < n:
                    area[4] += a[x][y]
                    continue

                area[5] += a[x][y]

        result = min(result, (max(area[1:])-min(area[1:])))




result = math.inf
for i in range(n):
    for j in range(n):
        points = boarders((i,j))
        area(points)

print(result)