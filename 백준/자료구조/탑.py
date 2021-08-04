N = int(input())
H = list(map(int, input().split()))
stack = []
for i in range(N):
    while stack:
        top = H[stack[-1]]
        if top > H[i]:
            break
        stack.pop()
    if stack == []:
        print(0)
    else:
        print(stack[-1]+1)
    stack.append(i)
