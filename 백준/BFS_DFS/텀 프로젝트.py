T = int(input())
def DFS(node):
    stack = [node]
    visited = []
    while stack :
        member = stack.pop()
        visited.append(member)
        next = team[member]

        if next not in visited :
            stack.append(next)
        else:
            index = visited.index(next)
            return visited, index

for _ in range(T):
    n = int(input())
    team = [0]
    team.extend(list(map(int,input().split())))

    org = [0]*(n+1)



    for i in range(1,n+1):

        next = team[i]

        if org[next] == 1 :
            org[i]=1
            continue
        if org[i] == 2:
            continue
        arr, index = DFS(i)
        #print(arr, index)
        for j in arr[:index]:
            org[j] = 1

        circled = arr[index:]

        for j in circled:
            org[j] = 2


    print(org.count(1))





