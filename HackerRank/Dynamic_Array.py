def dynamicArray(n, queries):

    lastAnswer = 0
    seq=[[] for _ in range(n)]

    for i in queries:
        x = i[1]
        y = i[2]

        if i[0] == 1:
            seq[((x^lastAnswer)%n)].append(y)
        else:
            seqIndex = ((x^lastAnswer)%n)

            lastAnswer = seq[seqIndex][y%(len(seq[seqIndex]))]
            print(lastAnswer)





first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
q = int(first_multiple_input[1])
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)