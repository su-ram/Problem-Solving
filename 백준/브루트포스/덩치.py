'''
자기 자신과 나머지 n-1명과 하나씩 비교해줘야 해서 브루트 포스
시간복잡도는 N**2 1:1로 비교해서 N**2
출력형식^^
'''

n = int(input())
bodys = [tuple(map(int, input().split()))for _ in range(n)]
ranking = [False] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if j == i:
            continue
        if bodys[i][0] < bodys[j][0] and bodys[i][1] < bodys[j][1]:
            cnt += 1
    ranking[i] = cnt + 1

for i in ranking:
    print(i, end=" ")