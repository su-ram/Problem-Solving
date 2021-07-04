from copy import  deepcopy
arr = [4,5,2,3,1]
k = 2
limit = len(arr)
pos = [-1] * (len(arr)+1)
for i in range(len(arr)):
    pos[arr[i]] = i

cnt = 0


def DFS(max, arr , cnt,ordered):
    print(max, arr, cnt, ordered)
    if ordered == limit:
        print("answer is ", cnt)

        return

    if max == arr.index(max)+1:
        DFS(max-1, arr, cnt,ordered+1)
        return

    for i in range(1, k+1):

        index = arr.index(max)

        if index+i < limit - ordered:

            new_arr = deepcopy(arr)
            new_arr[index], new_arr[index + i] = new_arr[index + i], new_arr[index]
            DFS(max, new_arr, cnt + 1, ordered)




DFS(max(arr), arr, 0, 0)
print(cnt)




