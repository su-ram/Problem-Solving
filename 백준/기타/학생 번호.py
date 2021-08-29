N = int(input())
ids = [input() for _ in range(N)]
start, end = 0, len(ids[0])
from collections import Counter

def isidentified(ids, offset):
    string_ids = list(map(lambda x : str(x[-offset:]), ids))
    counter = Counter(string_ids).items()
    if len(ids) != len(counter) :
        return False
    return True

while start <= end :
    mid = (start+end) // 2
    if isidentified(ids, mid) :
        result = mid if mid > 0 else result
        end = mid - 1
    else:
        start = mid + 1

print(result)

