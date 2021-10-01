import sys
input = sys.stdin.readline
S = input()
words = []
word = ''
tag = S.startswith('<')
for c in S:
    if tag:
        word += c
    if c == '>':
        tag = False
        words.append(word)
        word = ''
        continue
    if tag is False and c == '<':
        tag = True
        if word != '':
            word = word.split(' ')
            word = list(map(lambda x : x[::-1], word))
            words.append(' '.join(word))
        word = '<'
    if tag is False and c != '<':
        word += c

word = word.split(' ')
word = list(map(lambda x : x[::-1], word))
words.append(' '.join(word))

print(''.join(words))