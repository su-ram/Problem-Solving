from itertools import combinations_with_replacement
from collections import deque

T = int(input())

def pickPlates(n, k, p,plates):
    maximum = []
    temp = combinations_with_replacement(range(k+1),n)
    candi = []

    for i in temp:
        print(i)
        if sum(i) == p:
            candi.append(i)

    total = []
    for i in range(n):
        temp = []
        for j in range(k+1):
            temp.append(sum(plates[i][:j]))
        total.append(temp)


    for i in candi:
        pick = list(i)
        que = deque(pick)

        for j in range(n):

            que.append(que.popleft())
            hap = 0

            for k in zip(que,total):

                index = k[0]
                arr = k[1]

                hap += arr[index]
                maximum.append(hap)

    return maximum


for _ in range(T):
    n, k, p = map(int, input().split())
    plates = []

    for i in range(n):
        plates.append(list(map(int, input().split())))

    result = pickPlates(n,k,p,plates)

    print("Case #%d: %d"%(_+1,max(result)))