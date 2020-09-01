import collections
def arrayManipulation(n, q):
    array = [0] * (n + 1)

    for query in queries:
        print(array)
        a = query[0]-1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
    print(array)
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count

    return max_value

nm = input().split()
n = int(nm[0])
m = int(nm[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
print(result)