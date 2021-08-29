n, m = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))
b1, b2 = 0, 0
while b1 < n and b2 < m :
    if boxes[b1] >= books[b2]:
        boxes[b1] -= books[b2]
        b2 += 1
    else:
        b1 += 1
print(sum(boxes))

