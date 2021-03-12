def josephus(num, target):
    from collections import deque
    q = deque(list(range(1, num + 1)))
    order = []

    while q:
        value = q.popleft()
        q.append(value)
        value = q.popleft()
        q.append(value)
        order.append(q.popleft())

    return order


def main():
    print(josephus(15, 3))  # [3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다


if __name__ == "__main__":
    main()