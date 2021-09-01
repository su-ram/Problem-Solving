S = list(map(int, input().split()))
cnt = []
from collections import Counter
def dices(index, arr):
    if index == 3 :
        cnt.append(sum(arr))
        return
    for i in range(1, S[index]+1):
        dices(index+1, arr+[i])

dices(0,[])
most = Counter(cnt).most_common()
print(most[0][0])
