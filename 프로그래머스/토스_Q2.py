def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    if not sticky:
        for i in range(len(requests)):
            answer[i % servers].append(requests[i])
    else:
        head = 0
        counter = {}
        for i in range(len(requests)):
            head = head % servers
            request = requests[i]
            if counter.get(request) is None:
                answer[head].append(request)
                counter[request] = head
                head += 1
            else:
                answer[counter.get(request)].append(request)
    return answer

print(solution(4, False, [1,2,4,7,8,0,2,3,4,4,5,9,8,7]))