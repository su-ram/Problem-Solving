n = int(input())
names = []
for _ in range(n):
    names.append(input()[0])
from collections import Counter

counted = Counter(names)
result = [ c[0] for c in counted.items() if c[1] >= 5]
print(''.join(sorted(result)) if result != [] else 'PREDAJA')