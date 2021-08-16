n = int(input())
cnt = 0

def isdescending(num, l=None):
    global cnt, res
    string = num
    if len(string) == l :
        cnt += 1
        if cnt == n + 1 :
            print(num)
            exit(0)
    for i in range(10):
        if num == '':
            isdescending(string + str(i), l)
        elif i < int(string[-1]):
            isdescending(string + str(i), l)
res = []
ten = 1
while ten <= 10 :
    isdescending('', ten)
    ten += 1
print(-1)