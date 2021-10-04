counter = {"classic":{"total":1450,"ids":[[0,500],[2,150],[3,800]]},"pop":{"total":3100,"ids":[[1,600],[4,2500]]}}
for c in counter.keys():
    ids =counter.get(c).get('ids')
    ids = sorted(ids, key=lambda x: (x[1],-x[0]), reverse=True)
    counter[c]['ids'] = ids
result = sorted(counter.items(), key=lambda x:x[1]['total'], reverse=True)

arr = []
for gen in result:

    print(gen)
    cnt = 0
    for id in gen[1].get('ids'):
        if cnt == 2: break
        if len(arr) < 4:
            arr.append(id[0])
            cnt += 1
print(arr)