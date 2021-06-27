'''

'''

N = int(input())

def solution(N):
    cnt = 0
    num = 666
    while True:

        if str(num).count('666') >= 1:
            cnt += 1

        if cnt == N:
            break
        num += 1

    return num
