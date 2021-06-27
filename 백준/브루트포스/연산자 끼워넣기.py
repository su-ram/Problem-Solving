
operator = ['+', '-', '*', '/']

from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
operator = list(zip(operator, map(int, input().split())))
new_operator = []

for o in operator:
    new_operator.extend([o[0]]*o[1])

result = list(permutations(new_operator))
result = set(result)
calculated_value = set()

for op in result:
    x = nums[0]

    for i in range(n-1):

        y = nums[i+1]

        if op[i] == '+':
            x = (x+y)

        elif op[i] == '-':
            x = (x-y)

        elif op[i] == '*':
            x = (x*y)

        elif op[i] == '/':

            x = -((abs(x)//y))if x < 0 else (x//y)

    calculated_value.add(x)

print(max(calculated_value))
print(min(calculated_value))
