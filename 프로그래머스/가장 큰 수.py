
from itertools import permutations
import copy
def solution(numbers):
    answer = 'ㅎㅎ'
    numbers = [3, 30, 34, 5, 9]
    strings = [str(i)[0] for i in numbers]
    front_max=str(max(strings))
    candidate = []
    start = 0
    count = strings.count(front_max)
    for i in range(count):
        index = strings.index(front_max,start)
        candidate.append(index)
        start = index + 1
    for i in candidate:
        temp = copy.deepcopy(numbers)
        temp.pop(i)
        perm = permutations(temp,len(temp))
        for j in perm:
            print(j)



    return candidate


x = input()
print(solution(x))