def hourglassSum(arr):
    results=[]

    for i in range(4):
        for j in range(4):
            hap = arr[i+1][j+1]
            for k in range(3):
                hap += arr[i][j+k]
                hap += arr[i+2][j+k]
            results.append(hap)


    return max(results)

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)