N, M = map(int, input().split())
dduk = list(map(int, input().split()))
import math
answer = math.inf

def DdukLength(arr, target):
    total = 0
    for i in arr:
        if i > target:
            total += i - target

    return total


def BinarySearch(array, start, end):
    while start <= end:
        mid = (start+end) // 2
        if DdukLength(array, mid) == M:
            global answer
            answer = min(answer, mid)
            return mid
        elif DdukLength(array, mid) < M:
            end = mid - 1
        else:
            start = mid + 1
    return None

print(BinarySearch(dduk, 0, max(dduk)))

