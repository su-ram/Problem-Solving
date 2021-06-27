'''
N//2부터 시작해서 N-1까지 반복문으로 순회하면서 -> 브루트포스
조건을 만족하는 경우 result로 지정하고
모두 순회한 후에도 조건을 만족하지 못하면 0을 출력
'''

N = int(input())
result = False
for i in range(N):
    sum_tmp = 0
    for j in str(i):
        sum_tmp += int(j)

    if i + sum_tmp == N:
        result = i
        break

print(result if result else 0)