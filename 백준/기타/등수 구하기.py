N, score, P = map(int, input().split())
if N > 0:
    scores = list(map(int, input().split()))
    if N == P and score <= scores[-1] :
        print(-1)
        exit(1)
    elif N == P and score > scores[-1] :
        scores.pop()
    scores.append(score)
    scores.sort(reverse=True)
    print(scores.index(score)+1)
else:
    print(1)
