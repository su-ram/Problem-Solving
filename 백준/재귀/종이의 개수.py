N = int(input())
papers = [ list(map(int, input().split())) for _ in range(N)]
result = {-1:0, 0:0, 1:0}

def check(start, n):
    x,  y = start
    num = papers[x][y]
    for i in range(n):
        for j in range(n):
            if papers[x+i][y+j] != num : return False
    return True


def slice_paper(start, n):

    allsame = check(start, n)
    if allsame:
        num = papers[start[0]][start[1]]
        result[num] = result.get(num) + 1
        return

    length = n // 3
    x,y = start
    for i in range(3):
        for j in range(3):
            nx, ny = (x+i*length, y+j*length)
            slice_paper((nx,ny), length)


slice_paper((0,0), N)
for k, v in sorted(result.items()):
    print(v)