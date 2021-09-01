n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
issame = [[0]*(n+1) for _ in range(n+1)]
from collections import Counter
from itertools import combinations

def getstudent(students, _class):
    return [ i+1 for i in range(n) if students[i] == _class]

def connect(students):
    for s1, s2 in combinations(students, 2):
        if issame[s1][s2] == 0 :
            issame[s1][s2] = 1
        if issame[s2][s1] == 0 :
            issame[s2][s1] = 1


for i in range(5):
    grades = [ matrix[col][i] for col in range(n)]
    cnt = Counter(grades).most_common()
    cnt = [ c for c in cnt if c[1] > 1]
    for c in cnt :
        connect(getstudent(students=grades, _class=c[0]))


chef = (-1,-1)
for i in range(1, n+1):
    if sum(issame[i]) > chef[1] :
        chef = (i, sum(issame[i]))
print(chef[0])