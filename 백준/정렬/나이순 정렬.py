n = int(input())
names = [ list(input().split()) + [i] for i in range(n)]
names = sorted(names, key=lambda x : (int(x[0]), x[2]))

for n in names:
    print(n[0], n[1])