N = int(input())
H = list(map(int, input().split()))

stack = []

for i in range(N):
    node = H[i]
    if stack:
        while stack :
            if stack[-1][0] < node :
                stack.pop()
                if stack == []:
                    print("0", end=" ")
                    break

            elif stack[-1][0] > node :
                print(stack[-1][1] + 1, end=" ")
                break

            else:
                stack.pop()

        stack.append([node, i])
    else:
        print("0", end=" ")
        stack.append([node, i])