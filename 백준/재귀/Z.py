N, r, c = map(int, input().split())
cnt = 0

def search(n, start):
    x, y = start
    global cnt
    if n == 1 :
        print(cnt)
        return
    offset = n//2
    square = offset ** 2
    if x <= r < x + offset and y <= c < y + offset:
        cnt += square * 0
        search(n//2, (x, y))

    elif x <= r < x + offset and y <= c < y + 2 * offset:
        cnt += square * 1
        search(n//2, (x, y + offset))

    elif x + offset <= r < x + 2 * offset and y <= c < y + offset:
        cnt += square * 2
        search(n//2, (x + offset, y))

    elif x + offset <= r < x + 2 * offset and y <= c < y + 2 * offset:
        cnt += square * 3
        search(n//2, (x + offset, y + offset))


search(2**N, (0,0))
