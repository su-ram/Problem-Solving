n = int(input())
white = [ [0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(10):
        offset = 100 - (x+10)
        for j in range(10):
            white[offset+i][j+y] = 1
            
result = 0
for row in white:
    result += sum(row)
print(result)