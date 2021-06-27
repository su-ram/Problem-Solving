seen, heard = map(int, input().split())
people = []
from collections import Counter
for person in range(seen+heard):

    p = input()
    people.append(p)

counted = Counter(people)
both = []
for name, cnt in counted.items():
    if cnt == 2:
        both.append(name)

both.sort()
print(len(both))
for name in both:
    print(name)