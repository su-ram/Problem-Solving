def solution(amountText):
    answer = True
    if amountText.startswith(',') or amountText.endswith(','):
        return False
    splitted = amountText.split(',')
    if splitted[0].startswith('0'):return False
    for i in range(len(splitted)):
        if i > 0 and len(splitted[i]) != 3 :
            return False
        if not splitted[i].isdigit():
            return False

    return answer

print(solution('01,001,009'))