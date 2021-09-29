N, M = map(int,input().split())
#N개 중에 M을 고르는 수열

def solve(d,nums):

    if d == M:
        print(' '.join(map(str,nums)))
        return
    last = nums[-1] if d != 0 else 0
    for i in range(last+1, N+1):
        solve(d+1, nums+[i])

solve(0,[])