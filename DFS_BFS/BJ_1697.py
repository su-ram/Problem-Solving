#백준 1697 숨바꼭질
#이거 재귀로 풀어야 해!!!!
from collections import deque

#입력
n, k = map(int, input().split())
depth = 0
limit = k - n
limit = 2**limit*n

def sol(root):
    print(root)
    if root == 0 or root == 1: return 1
    else: return sol(root-1) + sol(root-2)

sol(n)