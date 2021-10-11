from collections import defaultdict

def solution(tickets):
    answer = []
    # defaultdict로 하면 되고 dict로 하면 안됨 ;;
    graph = defaultdict(list)
    for t in tickets:
        graph[t[0]].append(t[1])

    for key in graph:
        graph[key].sort()

    def dfs(node, path):
        if len(path) == len(tickets) + 1 :
            return path

        for i, city in enumerate(graph[node]):
            graph[node].pop(i)

            newPath = path[:]
            newPath.append(city)

            result = dfs(city,newPath)
            if result : return result

            graph[node].insert(i,city)


    answer = dfs('ICN',['ICN'])

    return answer




t = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
solution(t)

#["ICN", "COO", "ICN", "BOO", "DOO"]