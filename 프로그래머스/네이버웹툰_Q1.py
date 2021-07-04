lottery = [[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]]



def solution(lottery):
    record = {}
    for user in lottery:
        if record.get(user[0]) is None:
            record[user[0]] = [1, user[1]]
            continue
        value = record.get(user[0])
        if value[1] == 0 :
            value[0] += 1
            value[1] = user[1]
            record[user[0]] = value
    answer = [0,0]

    for user, result in record.items():
        if result[1] :
            answer[0] += result[0]
            answer[1] += 1
    return answer[0]//answer[1] if answer[1] > 0 else 0


print(solution(lottery))