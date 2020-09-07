MAX = 999999

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 지도를 N보다 사이즈가 1씩 큰 2차원 리스트로 생성한다.
    maze = [[MAX for i in range(N + 1)] for j in range(N + 1)]

    for i in range(N):
        # 지도를 한행씩 입력받는다.
        temp = list(map(int, input().split()))
        maze[i] = temp

        # 우측 패딩값을 999999로 설정한다.
        maze[i].append(MAX)

    for i in maze:
        print(i)

    # 지도를 패딩을 제외하고 가장 우측하단 도착지부터 왼쪽으로 순회한다.
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            # 도착지는 스킵한다.
            if i == N - 1 and j == N - 1:
                continue

            # 현재 위치에서 오른쪽과 아래를 비교해 더 빠른 경로를 찾는다.
            # 더 빠른경로의 값을 현재 위치에 더해 갱신한다.
            # 이렇게 하면 자연스레 모든 리스트의 값은 해당 위치에서 도착지까지의 최단경로값 형성되게 된다.
            if maze[i][j + 1] < maze[i + 1][j]:
                maze[i][j] = maze[i][j] + maze[i][j + 1]
            else:
                maze[i][j] = maze[i][j] + maze[i + 1][j]

    # 출발지 인덱스의 값을 출력한다.
