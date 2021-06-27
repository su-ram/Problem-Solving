
n = int(input())
results = [input() for _ in range(n)]
length = len(results[0])
command = ['']*length

for c in range(length):

    is_all_same = True

    for word in results[1:]:
        if word[c] != results[0][c]:
            is_all_same = False
            break

    if not is_all_same:
        command[c] = '?'

    else:
        command[c] = results[0][c]

print(''.join(command))