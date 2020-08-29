#Runner Up = 2등 선수

n = int(input())
arr = list(map(int, input().split()))
maxvalue = max(arr)
while maxvalue == max(arr):
    arr.remove(maxvalue)
print(max(arr))
