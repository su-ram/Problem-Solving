n = int(input())
cards = list(range(n))
player = [[] for _ in range(3)]
for i, p in enumerate(map(int, input().split())):
    player[p].append(i)

order = list(map(int, input().split()))

def shake(arr):
    new_arr = [0] * n
    for i in range(n):
        index = order[i]
        new_arr[index] = arr[i]
    global cards
    cards = new_arr


def give(arr):
    for i in range(n):
        if arr[i] not in player[i%3] : return False
    return True


cnt = 0
while not give(cards):
    shake(cards)
    cnt += 1
    if cards == list(range(n)):
        cnt = -1
        break

print(cnt)
