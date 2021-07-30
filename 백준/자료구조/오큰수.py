
N = int(input())
arr = list(map(int, input().split()))
stack = [0]
nums = [-1]*N

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        nums[stack.pop()] = arr[i]
    stack.append(i)

print(*nums)


# import copy
# N = int(input())
# arr = list(map(int, input().split()))
# stack = copy.deepcopy(arr[::-1])
# smaller = []
# nums = []
# for i in range(N-1):
#     while stack:
#         top = stack[-1]
#         if top < arr[i] :
#             smaller.append(top)
#             stack.pop()
#         elif top == arr[i]:
#             stack.pop()
#             continue
#         elif top > arr[i]:
#             break
#
#     if stack != []:
#         nums.append(str(stack[-1]))
#         while smaller:
#             smaller.pop()
#     else:
#         nums.append(str(-1))
#         while smaller:
#             stack.append(smaller.pop())
#
# print(' '.join(nums+['-1']))