from itertools import combinations
test_case = int(input())

def CanIBuy(combi, limit):
    for i in combi:
        if sum(i) <= limit:return True
    return False
def KnapSack(n, limit, value):

    maximum = 0
    value=sorted(value)
    total = 0
    for i in value:
        total += i
        if total <= limit:
            maximum+=1


    return maximum


for _ in range(test_case):
    n, limit = map(int, input().split())
    value = list(map(int, input().split()))
    result = KnapSack(n, limit, value)
    print("Case #%d: %d" % (_ + 1, result))
