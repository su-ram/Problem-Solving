n = int(input())
arr = [int(input()) for _ in range(n)]
sorted_arr = sorted(arr)
print(round(sum(arr) / n))
print(sorted_arr[n//2])
from collections import Counter
counter = Counter(arr).most_common()
most_common = counter[0][1]
counter = [ c for c in counter if c[1] == most_common]
if len(counter) > 1 :
    print(sorted(counter, key=lambda x : x[0])[1][0])
else: print(counter[0][0])
print(sorted_arr[-1] - sorted_arr[0])
