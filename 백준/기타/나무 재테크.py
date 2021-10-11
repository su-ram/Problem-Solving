from collections import defaultdict
import heapq


n, m, k = map(int, input().split())
A = []
A = [[0]+(list(map(int, input().split()))) for _ in range(n)]
trees = [list(map(int, input().split())) for _ in range(m)]
A.insert(0,[])

def solution(n, m, k, A, trees):
    # tree[i][j][0] = 해당 위치의 양분 양
    # tree[i][j][1:] = 나무 나이들
    tree = [ [[5] for _ in range(n+1)] for _ in range(n+1)]
    dx = [-1, -1, -1, 0, 0, +1, +1, +1]
    dy = [-1, 0, +1, -1, +1, -1, 0, +1]

    for i, j, v in trees:
        tree[i][j].append(v)


    for _ in range(k):
    #봄
        for i in range(1, n+1):
            for j in range(1, n+1):
                dead = 0
                aged = tree[i][j][1:]
                temp = []
                if len(aged) >= 1:
                    aged.sort()
                    for a in aged:
                        if a <= tree[i][j][0]:
                            tree[i][j][0] -=a
                            temp.append(a+1)
                        else:
                            dead += a// 2

                tree[i][j][1:] = temp
                #여름
                tree[i][j][0] += dead

        #가을
        for i in range(1, n+1):
            for j in range(1, n+1):
                for a in tree[i][j][1:]:
                    if a % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if 1 <= nx <= n and 1 <= ny <= n:
                                tree[nx][ny].append(1)

        #겨울
        for i in range(1, n+1):
            for j in range(1, n+1):
                tree[i][j][0] += A[i][j]

    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            ans += len(tree[i][j][1:])

    return ans





print(solution(n, m, k,A, trees))