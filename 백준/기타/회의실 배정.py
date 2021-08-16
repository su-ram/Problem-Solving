n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
times = sorted(times, key=lambda x : (x[1], x[0]))
meeting = [times[0]]
print(times)
for i in range(1, n):
    now = times[i]
    if now[0] >= meeting[-1][-1]:
        meeting.append(now)
print(len(meeting), meeting)