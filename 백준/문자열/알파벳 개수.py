word = input()
counts = ['0'] * 26
for s in word:
    index = ord(s) - ord('a')
    count = int(counts[index])+1
    counts[index] = str(count)
print(' '.join(counts))