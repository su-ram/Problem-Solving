n = int(input())
votes = [int(input()) for _ in range(n)]
import heapq
def election(n, votes):
    if n == 1 :
        return 0

    dasom = votes[0]
    votes = votes[1:]
    votes.sort(reverse=True)
    cnt = 0
    while dasom < votes[0] :
        adds = (votes[0] - dasom)//2 + (1 if (votes[0] - dasom) % 2 else 0 )
        dasom += adds
        votes[0] -= adds
        votes.sort(reverse=True)
        cnt += adds
    return cnt

print(election(n, votes))