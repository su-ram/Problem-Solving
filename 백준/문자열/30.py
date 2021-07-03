N = input()
zeros = N.count('0')

def solution(N):
    if zeros:
        N = N.replace('0','')
        N = list(N)
        N.sort(reverse=True)
    else:
        return -1

    max_num = -1
    num = int(''.join(N))
    if num % 3 == 0 and num > max_num:
        max_num = num

    return max_num * (10 ** int(zeros)) if max_num != -1 else max_num

print(solution(N))