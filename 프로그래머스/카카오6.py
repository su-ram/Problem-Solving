def solution(board, skill):
    answer = 0
    position = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            pos = str(i)+'/'+str(j)
            position[pos] = board[i][j]

    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1 :
            degree *= -1
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                pos = str(i) + '/' + str(j)
                position[pos] += degree
    print(position.values())
    for i in position.values():
        if i > 0 :
            answer += 1
    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board, skill))