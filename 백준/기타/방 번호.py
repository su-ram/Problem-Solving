num = input()
from collections import Counter
counter = Counter(num)
sixnine = 0
others = 0
for c in counter.items():
    if c [0] in ['6', '9']:
        sixnine += c[1]
    else:
        others = max(others, c[1])
print(max(sixnine//2 + sixnine%2, others))