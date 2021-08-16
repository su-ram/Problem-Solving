n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def issamecolor(start, length):
    color = arr[start[0]][start[1]]
    for i in range(length):
        row = arr[i+start[0]][start[1]:start[1]+length]
        for j in row:
            if j != color:
                return False
    return True

def colored_paper(start, length):
    if length == 1:
        if arr[start[0]][start[1]] :
            global white
            white += 1
        else:
            global blue
            blue += 1
        return
    if issamecolor(start, length):
        if arr[start[0]][start[1]] :
            white += 1
        else:
            blue += 1
    else:
        colored_paper((start[0], start[1]), length//2)
        colored_paper((start[0] + length//2, start[1]), length//2)
        colored_paper((start[0], start[1] + length//2), length//2)
        colored_paper((start[0] + length//2, start[1] + length//2), length//2)


colored_paper((0,0), n)
print(blue)
print(white)
