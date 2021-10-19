
from collections import deque, defaultdict
def solution(leaves, day, holidays):
    answer = -1
    if day == 'MON':
        weekend = [6,7]
    elif day == 'TUE':
        weekend = [5,6]
    elif day == 'WED':
        weekend = [4,5]
    elif day == 'THU':
        weekend = [3,4]
    elif day == 'FRI':
        weekend = [2,3]
    elif day == 'SAT':
        weekend = [1,2]
    else:
        weekend = [1,8,9]
    for _ in range(5):
        sat, sun = weekend[-2:]
        if sat + 7 <= 30:
            weekend.append(sat+7)
        if sun + 7 <= 30:
            weekend.append(sun+7)

    weekend = set(weekend)
    weekend.update(holidays)
    days = [0]*31
    for d in weekend:
        days[d] = 1

    s = 0
    e = 1
    serial = 0
    que = deque()
    cnt = 0
    for day in days[1:]:
        if not serial and day:
            serial = 1
        elif serial and day:
            serial += 1
        if day == 0:
            cnt = max(cnt, serial)
            serial = 0

    while s <= 30:
        if e > 30:
            s += 1
            continue
        if days[e] == 0:
            e += 1
            continue
        if days[e] == 1 and len(que) < leaves:
            que.append(e)
        elif days[e] == 1 and len(que) == leaves and que:
            front = que.popleft()
            serial = max(serial, e - front, e - 1 - s)
            s = front
            que.append(e)

        e += 1
    serial = max(serial, e-s)

    print(days, serial)
    return answer



solution(2, "WED", [1,4,18,29])