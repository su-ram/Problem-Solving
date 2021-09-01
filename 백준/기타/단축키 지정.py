n = int(input())
shortcuts = [0] * (26)
for _ in range(n):

    shorted = []
    options = input().split()
    shortcut = False

    #각 단어의 첫문자를 검사한다.
    for op in options:
        if shortcut :
            shorted.append(op)
            continue

        alpha = ord(op[0].lower()) - 97
        if shortcuts[alpha] == 0 :
            shortcut = True
            shortcuts[alpha] = 1
            op = op.replace(op[0], '['+op[0]+']', 1)
        shorted.append(op)

    if not shortcut:
        shorted.clear()

        for op in options:
            if shortcut:
                shorted.append(op)
                continue

            for c in op:
                alpha = ord(c.lower()) - 97
                if shortcuts[alpha] == 0:
                    shortcuts[alpha] = 1
                    shortcut = True
                    op = op.replace(c, '[' + c + ']', 1)
                    break
            shorted.append(op)


    print(' '.join(shorted))
