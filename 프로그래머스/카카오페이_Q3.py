def string_check(formatted, origin, index):

    issame = True
    for i in range(len(formatted)):

        if formatted[i] == '_':continue
        if i + index >= len(origin) :
            return False
        if formatted[i] != origin[i+index] :
            return False
    return issame



def solution(line1, line2):
    answer = 0

    limit = (len(line1) - len(line2)) // 2
    for i in range(limit+1):
        under_bar = '_' * (i)
        formatted=under_bar.join(line2)

        start = 0
        while start < len(line1):

            if line1[start] == formatted[0]:
                if string_check(formatted, line1, start):
                    answer += 1
                    print(formatted, line1, start)

            start += 1


    return answer


inputs = [["abacaba", "acb"]]

for i in inputs:
    solution(i[0], i[1])