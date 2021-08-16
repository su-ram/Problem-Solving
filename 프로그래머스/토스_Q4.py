def solution(input):
    answer = ''
    cmd = input.split('\n')
    print(cmd)
    days = 1
    counts = 0
    isshow = True
    for c in cmd:
        if len(c.split()) == 2:
            n, m = map(int, c.split())
        elif c == 'SHOW':
            if isshow:
                print('1')
                counts += 1
                if counts == m and days <= n :
                    isshow = False
                    counts = 0
                    days = 1
            else:
                print('0')

        elif c == 'NEGATIVE':
            counts += 1
            if counts <= m and days <= n :
                isshow = False
                days = 1
                counts = 0
            print('0')
        elif c == 'NEXT':
            if days == n :
                days = 1
                counts = 0
                if not isshow :
                    isshow = True
            else:
                days += 1
            print('-')
        elif c == 'EXIT':
            print('BYE')
        else:
            print('ERROR')


print(solution('2 3\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nEXIT'))