def solution(program, flag_rules, commands):

    answer = []
    rules = {}  # flag - flag의 인자 타입을 key-value 값으로 저장

    # flag을 key로 하여 인자 타입을 value로 하여 딕셔너리로 저장한다.
    for rule in flag_rules:
        splitted_rule = rule.split()

        if len(splitted_rule) == 2:
            flag, arg = splitted_rule

            if flag in rules:
                alias = rules[flag]
                rules[alias] = arg
            rules[flag] = arg
        else:
            alias = splitted_rule[0]
            flag = splitted_rule[-1]
            rules[flag] = alias

    print(rules)

    for command in commands:
        splitted_command = command.split()
        program_name = splitted_command[0]

        # 프로그램명을 다르게 입력한 경우는 올바르지 않은 형식이다.
        if program_name != program:
            answer.append(False)
            continue

        flag = False
        isvalid = True # 입력된 명령어가 인자값 형식이랑 맞는지 유효성 검사.

        for index in range(1, len(splitted_command)):

            #flag인지 flag_argument인지 판별
            if splitted_command[index].startswith('-'):
                flag = splitted_command[index]
                num_argument = 0
                isvalid = True

            #flag_argument이지만 앞서 flag가 입력되지 않은 경우는 유효하지 않다.
            elif not flag:
                isvalid = False

            # 앞서 입력된 flag가 규칙에 없는 flag인 경우는 유효하지 않다.
            elif flag not in rules:
                isvalid = False

            # 앞서 입력된 flag가 flag_argument를 필요로 하지 않을 경우 다음으로 넘어간다.
            elif rules[flag] == 'NULL':
                continue

            else:
                # 인자값 형식에 대하여 유효성 검사를 한다.
                argument = splitted_command[index]
                num_argument += 1

                if rules[flag].startswith('NUMBER'):

                    if num_argument > 1 and not rules[flag].endswith('S'):
                        isvalid = False

                    elif rules[flag].endswith('S') or num_argument == 1:
                        isvalid = argument.isdigit()

                if rules[flag].startswith('STRING'):

                    if num_argument > 1 and not rules[flag].endswith('S'):
                        isvalid = False

                    elif rules[flag].endswith('S') or num_argument == 1:
                        isvalid = argument.isalpha()


            if isvalid == False:
                break

        answer.append(isvalid)


    return answer




program = "trip"
flag_rules = ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]
commands = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]
print(solution(program, flag_rules, commands))
