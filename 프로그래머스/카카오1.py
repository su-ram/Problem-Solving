def solution(id_list, report, k):
    answer = [0] * len(id_list)
    counter = [ [] for _ in range(len(id_list))]
    ids = {}

    for i in range(len(id_list)):
        ids[id_list[i]] = i


    for r in report:
        s, t = r.split()
        index = ids.get(t)
        if ids.get(s) not in counter[index]:
            counter[index].append(ids.get(s))

    for cnts in counter:
        if len(cnts) >= k :
            for index in cnts:
                answer[index] += 1

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))