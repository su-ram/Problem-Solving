from collections import Counter, deque

def solution(research, n, k):

    days = len(research)
    search = {}
    result = {}

    for i in range(26):
        search[chr(i+97)] =[0]*days


    for day in range(days):
        counter = Counter(list(research[day])).items()
        for w, c in counter:
            search[w][day] = search.get(w)[day] + c

    for word, cnt in search.items():
        que = deque()

        serial = True
        total = 0
        for c in cnt:
            if c < k :
                serial = False
            else:
                serial = True
            que.append(c)
            if len(que) == n :
                if sum(que) >= 2 * n * k and serial:total += 1
                que.popleft()
        result[word] = total
    print(result)
    result = Counter(result).most_common()
    print(result)
    return result[0][0] if result[0][1] else "None"


r = ["yxxy","xxyyy","yz"]
n = 2
k = 1
print(solution(r, n, k))