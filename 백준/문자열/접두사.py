N = int(input())
string = [input() for _ in range(N)]
result = 1
prev = []
for s in string:
    if s in prev:continue
    subset = [s]

    for other in string:
        if other == s: continue
        prefix = False
        for sub in subset:
            if sub.startswith(other) or other.startswith(sub):
                prefix = True
                break
        if not prefix:
            subset.append(other)
    prev = subset
    result = max(result, len(subset))
    print(subset)
print(result)