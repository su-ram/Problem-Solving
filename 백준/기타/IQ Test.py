n = int(input())
arr = list(map(int, input().split()))
result = False
if len(arr) > 2 :
    a , b = divmod(arr[2], arr[1])
    for i in range(n-1):
        if arr[i+1] != arr[i]*a + b:
            result = 'B'
            break
    print(arr[-1]*a + b if not result else result)
elif len(arr) == 2 :
    print('A')
else:
    print('B')