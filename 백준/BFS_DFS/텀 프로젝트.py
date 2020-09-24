T = int(input())

for _ in range(T):
    n = int(input())
    team = [0]+(list(map(int,input().split())))
    visit=[0]*(n+1)

    group = 1

    for i in range(1,n+1):
        if visit[i] == 0:
            while visit[i] == 0 :
                visit[i] = group
                i = team[i]
            while visit[i] == group:
                visit[i] = -1
                i = team[i]
            group += 1

    cnt = 0
    for j in visit:
        if j >0 :
            cnt +=1
    print(cnt)