
n = int(input())
dices = [0] * (n+1)


def stack(order, bottom):
    total = 0
    global n

    for o in order:
        top = dices[o].get(bottom)
        if 6 not in [top, bottom]:
            total += 6
        elif 5 not in [top, bottom]:
            total += 5
        else:
            total += 4
        bottom = top

    return total


for i in range(n):
    nums = list(map(int, input().split()))
    maps = {}
    maps[nums[0]] = nums[5]
    maps[nums[5]] = nums[0]
    maps[nums[1]] = nums[3]
    maps[nums[3]] = nums[1]
    maps[nums[2]] = nums[4]
    maps[nums[4]] = nums[2]
    dices[i+1] = maps


result = -1
for i in range(1,7):
    result = max(result, stack(range(1,n+1),i))
print(result)
