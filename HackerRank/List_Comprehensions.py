#입력

x = int(input())
y = int(input())
z = int(input())
n = int(input())

#모든 조합의 수 만들기
permutation=[]

for i in range(x+1):

    for j in range(y+1):

        for k in range(z+1):

            if i+j+k != n:
                permutation.append([i, j, k])

print(permutation)



