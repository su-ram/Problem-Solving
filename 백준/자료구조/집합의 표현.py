n, m = map(int, input().split())
idx = [i for i in range(n+1)]

def get_parent(a):

    if idx[a] == a:
        return a
    else:
        return get_parent(idx[a])

def union(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)

    if parent_a == parent_b:  # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if parent_a < parent_b:  # a와 b의 루트 노드가 다르면 두 집합을 합치기
        idx[parent_b] = parent_a
    else:
        idx[parent_a] = parent_b



for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0 :
        union(a, b)

    else:
        if get_parent(a) == get_parent(b):
            print('YES')
        else:
            print('NO')

print(idx)



