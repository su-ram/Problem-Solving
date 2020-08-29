n = int(input())
records={}
for i in range(n):
    name, *scores = input().split()
    records[name] = list(map(float,scores))
name = input()
results = records[name]
results = sum(results) / len(results)
print("%.2f" % results)
