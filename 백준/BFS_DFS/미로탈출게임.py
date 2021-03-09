from collections import deque

def BFS(dist):

    que = deque()
    que.append((0,0))
    dist[0][0] = 1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    candidate = []

    while len(que) != 0 :

        node = que.popleft()

        if node[0] == N-1 and node[1] == N-1 :
            continue

        for i in range(4):

            xx = node[0] + dx[i]
            yy = node[1] + dy[i]

            if N > xx >= 0 and N > yy >= 0 and dist[xx][yy] == 0 and matrix[xx][yy] == 1:
                que.append((xx,yy))

                if xx == N -1 and yy == N - 1:
                    candidate.append(dist[node[0]][node[1]]+1)
                    continue

                dist[xx][yy] = dist[node[0]][node[1]] + 1






    return candidate


def solution():

    dist = []
    [dist.append([0]*N) for i in range(N)]
    return min(BFS(dist))




if __name__ == '__main__':
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input())))

    print(solution())
