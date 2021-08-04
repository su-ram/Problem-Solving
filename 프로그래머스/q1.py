
color = ["BW", "RY", "BY"]
prices = [9000, 10000]
def solution(color, prices):
    answer = 0
    counter = {"R" : 0, "B" : 0, "G":0, "Y":0, "W":0}
    candidates = [len(color)*prices[1]]
    for c in color:
        counter[c[0]] += 1
        counter[c[1]] += 1
    same, diff = 0, 0
    for v in counter.values():
        same += v // 2
        diff += v % 2
    candidates.append(same*prices[0]+(diff//2)*prices[1])
    candidates.append((same+diff)*prices[0])
    print(candidates)
    return min(candidates)

print(solution(color, prices))