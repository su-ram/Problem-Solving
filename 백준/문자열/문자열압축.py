def solution(s):
    answer = []
    stripped = s[1:-1].split('},{')
    stripped[0] = stripped[0][1:]
    stripped[-1] = stripped[-1][:-1]

    stripped = sorted(stripped, key=lambda x: len(x))
    prev = int(stripped[0])
    answer.append(prev)
    for string in stripped[1:]:
        nums = string.split(',')
        nums = list(map(int, nums))
        for i in range(len(answer)):
            nums.remove(answer[i])
        answer.append(nums[0])
    print(answer)
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")