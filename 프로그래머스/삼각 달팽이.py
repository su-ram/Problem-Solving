def circle(num, offset, length, a):

    for i in range(length):
        a[2 * offset + i + 1][offset] = num
        num += 1
    for i in range(length - 1):
        a[- 1 - offset][i + 1 + offset] = num
        num += 1
    for i in range(1, length - 1):
        a[-i -1 -offset][-offset - 1] = num
        num += 1

    return num


def solution(n):
    a = [[0] * i for i in range(n + 1)]
    length = n
    offset = 0
    num = 1
    while length > 0:
        num = circle(num, offset, length, a)
        offset += 1
        length -= 3


solution(80)


import heapq
heapq.h
