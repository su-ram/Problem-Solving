# second lowest grade.

records = {}
names = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in records.keys():
        temp = records[score]
        temp.append(name)
        records[score] = temp
    else:
        records[score] = [name]
lowest = min(records.keys())
second = False
for i in sorted(records.keys()):
    if i > lowest and not second :
        second = True
        names.extend(records[i])


for i in sorted(names):
    print(i)