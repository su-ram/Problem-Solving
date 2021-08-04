N = int(input())
import sys
input = sys.stdin.readline

def make_combinations(index, arr, limit):
    if index == limit:
        return
    for i in items[index]:
        global cnt
        cnt += 1
        for j in range(limit - index):
            make_combinations(index+1+j, arr + [i], limit)

for _ in range(N):
    cloths = {}
    for _ in range(int(input())):
        cloth, category = input().split()
        if not cloths.get(category) :
            cloths[category] = [cloth]
        else:
            new = cloths.get(category)
            new.append(cloth)
            cloths[category] = new


    cases = 1
    for v in cloths.values():
        cases *= (len(v)+1)
    print(cases-1)

    items = []
    # for k, v in cloths.items():
    #     items.append(list(range(len(v))))
    # cnt = 0
    # for i in range(len(items)):
    #     make_combinations(i, [], len(items))
    # print(cnt)