def solution(dirs):
    visited = set()
    d = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    x, y = 0, 0
    ans = 0
    log = [(x, y)]
    for dir in dirs:
        dx, dy = d.get(dir)
        nx = x + dx
        ny = y + dy
        forward = str(x)+str(y)+str(nx)+str(ny)
        backward = str(nx)+str(ny) + str(x)+str(y)

        if abs(nx) > 5 or abs(ny) > 5:
            continue

        if forward not in visited and backward  not in visited:
            ans += 1
            visited.add(forward)
            visited.add(backward)
        else:
            visited.add(forward)
            visited.add(backward)

        x = nx
        y = ny

    return log, ans


dirs = "UUUUDUDUDUUU"
print(solution(dirs))