def matchingStrings(strings, queries):

    cnts=[]

    for i in queries:

        num = 0

        for j in strings:
            if j == i : num +=1

        cnts.append(num)

    return cnts

strings_count = int(input())
strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(strings, queries)

for i in res:
    print(i)
