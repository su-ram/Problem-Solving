from itertools import permutations

def solution(k,m):
    answer = 0
    cadidates = permutations(range(1, k+1),k)
    for c in cadidates:
        num = ''
        for n in c:
            num += str(n)
            print(int(num))
        if int(num) % m == 0:
            answer += 1
    print(answer)



solution(5,1)