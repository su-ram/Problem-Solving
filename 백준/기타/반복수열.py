
A, P = map(int, input().split())


def solution(A, P):
    arr = [A]
    while True:
        numstr = str(arr[-1])
        n = 0
        for c in numstr:
            n += int(c)**P
        if n in arr:
            print(arr, n)
            return arr.index(n)
        arr.append(n)

    return len(arr)

print(solution(A, P))