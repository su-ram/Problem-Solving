N, m, M, T, R = map(int, input().split())

def run(now):
    global sec
    sec +=1
    return now + T


def breaktime(now):
    return now - R if now - R >= m else m


now = m
sec = 0
total = 0
if m + T > M :
    print(-1)
    exit(0)
while True :
    if now > M or now < m or sec == N :
        print(total if sec == N else -1)
        break
    if now + T <= M:
        now = run(now)
    else:
        now = breaktime(now)
    total += 1

