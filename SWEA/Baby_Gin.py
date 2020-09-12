T = int(input())

def isrun(arr):
    cnt = 0
    for i in arr:
        if i == 1:
            cnt += 1
        elif i == 0:
            if cnt >= 3:
                return True
            cnt = 0
    return False

def triplet(cnt):
    for i in cnt:
        if i >= 3: return True
    return False

for i in range(T):

    num = list(map(int, input().split()))

    p1 = [0] * 10
    p2 = [0] * 10
    cnt1 = [0] * 10
    cnt2 = [0] * 10

    for j in range(6):
        a, b = num[2*j+0], num[2*j + 1]
        winner = []
        p1[a] = 1
        p2[b] = 1
        cnt1[a] += 1
        cnt2[b] += 1
        if j >= 2:
            if isrun(p1) or triplet(cnt1):
                winner.append(1)
            if isrun(p2) or triplet(cnt2):
                winner.append(2)

            if len(winner) == 1:
                print("#%d %d" %(i+1, winner[0]))
                break
    if len(winner) == 0 or len(winner) == 2:
        print("#%d %d"%(i+1, 0))

