n = int(input())
shortcuts = [0] * (26)
for _ in range(n):
    shortcut = ''
    shorted = []
    options = input().split()
    for option in options:
        index = ord(option[0].lower()) - 97
        if shortcuts[index] == 0 and shortcut == '':
            shortcuts[index] = 1
            shortcut = option[0]
            shorted.append('['+option[0]+']'+option[1:])
            continue
        shorted.append(option)

    if shortcut == '':
        shorted.clear()
        for option in options:
            if len(option) == 1 :
                shorted.append(option)
                continue

            if shortcut == '':
                for c in option[1:]:
                    index = ord(c.lower()) - 97
                    if shortcuts[index] == 0 :
                        shortcuts[index] = 1
                        shortcut = c
                        index = option.index(shortcut)
                        shorted.append(option[:index] + '[' + shortcut + ']' + option[index+1:])
                        break
            else : shorted.append(option)

    print(' '.join(shorted) if shortcut != '' else ' '.join(options))


