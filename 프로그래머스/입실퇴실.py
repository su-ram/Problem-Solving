from collections import deque


def solution(enter, leave):
    n = len(enter)
    enter = deque(enter)
    leave = deque(leave)
    answer = [0] * (n + 1)
    room = []
    new = []

    while leave:
        if leave[0] in room:
            room.remove(leave[0])
            leave.popleft()
            continue

        while enter:
            if enter[0] == leave[0]:
                new.append(enter.popleft())
                break
            new.append(enter.popleft())

        total = len(room) + len(new)
        for r in room:
            answer[r] += len(new)
        for _n in new:
            answer[_n] += total - 1

        room.extend(new[:-1])
        new.clear()
        leave.popleft()

    return answer[1:]


enter = [1,4,2,3]
leave = [2,1,3,4]

print(solution(enter, leave))