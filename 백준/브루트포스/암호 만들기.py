L, C = map(int, input().split())
characters = list(input().split())
vowels = set(['a', 'e', 'i', 'o', 'u'])
from itertools import combinations, permutations

characters.sort()
candidates = combinations(characters,L)

# for c in candidates:
#
#     print(c)
#     vowwl_check = vowels.intersection(c)
#
#     if len(vowwl_check) < 1 or len(vowwl_check) > L-2:
#         continue
#
#     isordered = True
#
#     for i in range(L-1):
#         if c[i+1] < c[i] :
#             isordered = False
#             break
#
#     if not isordered:
#         continue
#
#     #print(''.join(c))


def DFS(index):
    out.append(characters[index])
    if len(out) == L :
        num_vowles = vowels.intersection(out)
        if 1 <= len(num_vowles) <= L - 2:
            print(''.join(out))
        return
    for i in range(index+1, C):
        DFS(i)
        del out[-1]

for j in range(C):
    out = []
    DFS(j)