T = int(input())
def solution(start, times):
    start_time = start[1]
    result = [25,25]
    for i in times:
        next_start = i
        if next_start[0] >= start_time and next_start[1] <result[1]:
            result = next_start

    return result

for i in range(T):
    times =[]
    N = int(input())
    for _ in range(N):
        times.append(list(map(int, input().split())))
    temp = sorted(times, key=lambda x: x[1])
    start = temp[0]
    cnt = 1
    temp.remove(start)
    while True :
        next = solution(start,temp)
        if next == [25,25] : break
        else:
            start = next
            temp.remove(next)
            cnt += 1
    print("#%d %d" % (i+1, cnt))
