from collections import defaultdict

def solution(gems):
    answer = []
    types = set(gems)
    s , e = 0, 0
    cnt = defaultdict(int)

    while s <= e and e < len(gems):

        if len(cnt) == len(types):
            answer.append((s+1,e))
            if cnt[gems[s]] ==1:
                cnt.pop(gems[s])
            elif cnt[gems[s]] > 1:
                cnt[gems[s]] -= 1
            s += 1
        else:
            cnt[gems[e]] += 1
            e += 1


    while s < len(gems):

        if len(cnt) == len(types):
            answer.append((s+1,e))
        if cnt[gems[s]] ==1:
            cnt.pop(gems[s])
        elif cnt[gems[s]] > 1:
            cnt[gems[s]] -= 1
        s += 1

    answer.sort(key=lambda x : (x[1]-x[0], x[0]))

    return answer


gems = ["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]
solution(gems)