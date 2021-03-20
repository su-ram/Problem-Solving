def solution(enter, leave):
    n = len(enter)
    answer = [0] * n

    for i in range(n):
        enter_i = enter.index(i + 1)
        leave_i = leave.index(i + 1)

        for j in range(i + 1, n):
            enter_j = enter.index(j + 1)
            leave_j = leave.index(j + 1)
            print(enter_i, enter_j, leave_i, leave_j)
            enter_order = enter_i < enter_j
            leave_order = leave_i < leave_j
            if enter_order != leave_order:

                answer[i] += 1
                answer[j] += 1
                print(answer)

    return answer
print(solution([1,4,2,3],[2,1,3,4]))