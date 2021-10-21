

#1
# def solution(day, k):
#     firstdays = [day]
#     first = day
#     answer = []
#     days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
#     for month in days:
#         plus = month % 7
#         plus = (first+plus) % 7
#         firstdays.append(plus)
#         first = plus
#
#     for d in firstdays:
#         diff = k - 1
#         diff = diff % 7
#         plus = (d+diff) % 7
#         if plus > 4:
#             answer.append(1)
#         else:
#             answer.append(0)
#     print(firstdays)
#     print(answer)


# from collections import Counter
# def solution(card, word):
#
#     answer = []
#     for w in word:
#         cnt = dict(Counter(w).most_common())
#         check = [False] * 3
#         for i in range(3):
#             cardkeys = dict(Counter(card[i]).most_common())
#             for k in cnt.keys():
#                 if k in cardkeys.keys():
#                     check[i] = True
#                     cnt[k] -= cardkeys[k]
#
#         available = True
#         if sum(check) != 3 :
#             available = False
#         for v in cnt.values():
#             if v > 0:
#                 available = False
#                 break
#         if available:
#             answer.append(w)
#
#
#     return answer if answer != [] else ["-1"]




from collections import deque, defaultdict


def solution(customer, K):

    room = {}
    waiting = deque()
    cancel = defaultdict(int)

    for id, req in customer:
        if req :
            if len(room) < K:
                room[id] = True
            else:
                #남는 방이 없을 경우
                waiting.append(id)

        #예약
        else:
            #취소
            if id in room:
                room.pop(id)
                if waiting:
                    while cancel[waiting[0]]:
                        cancel[waiting[0]] -= 1
                        waiting.popleft()
                    room[waiting.popleft()] = True
            else:
                cancel[id] += 1



            #방이 하나 남고, 대기자가 있는 경우
    # 3
    # 12
    answer = list(room.keys())
    answer.sort()
    print(answer)
    return answer

solution([[2,1],[1,1],[3,1],[1,0],[1,1],[2,0],[2,1]], 1)