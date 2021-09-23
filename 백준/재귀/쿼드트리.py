N = int(input())
matrix = [list(input()) for _ in range(N)]
result = ''


def issame(x,y,n):
    start = matrix[x][y]
    for i in range(n):
        for j in range(n):
            if matrix[i+x][j+y] != start:
                return False
    return True


def solve(x,y,n):
    check = issame(x,y,n)
    global result
    if check :
        result += (matrix[x][y])
        return

    result += ('(')
    solve(x, y, n//2)
    solve(x, y+n//2, n//2)
    solve(x+n//2, y, n//2)
    solve(x+n//2, y+n//2, n//2)
    result += (')')

solve(0,0,N)
print(result)