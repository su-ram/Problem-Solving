
from collections import defaultdict
import datetime, math

def solution(fees, records):
    format = '%H:%M'
    free = fees[0]
    fee = fees[1]
    answer = []
    times = {}
    counter = defaultdict(int)

    for r in records:
        time, id, cmd = r.split()
        if cmd == 'IN':
            times[id]=(datetime.datetime.strptime(time, format))
        else:
            enter = times[id]
            out = datetime.datetime.strptime(time, format)
            minutes = (out-enter).seconds//60

            counter[id] += minutes
            times[id] = False

    for id, time in times.items():
        if time is not False:
            enter = time
            out = datetime.datetime.strptime("23:59", format)
            minutes = (out-enter).seconds // (60)
            counter[id] += minutes

    for id, time in counter.items():
        if time <= fees[0]:
            answer.append((id,fees[1]))
        else:
            add = math.ceil((time - fees[0]) / fees[2])
            add *= fees[3]
            add += fees[1]
            answer.append((id,add))
    answer.sort(key=lambda x : x[0])
    return [ a[1] for a in answer]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

print(solution(fees,records))