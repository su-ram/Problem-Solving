import sys
input = sys.stdin.readline
S = input()
words = []
word = ''
tag = False
for c in S:
    if not tag and c == '<':

        word = word.split()
        while word.count('') :
            word.remove('')

        word = list(map(lambda x : x[::-1], word))
        words.extend(' '.join(word))
        word = c
        tag = True
    elif not tag and c != '<':
        word += c
    elif tag and c != '<' and c != '>':
        word += c
    elif tag and c == '>':
        word += c
        words.append(word)
        tag=False
        word = ''
if word:
    word = word.split(' ')
    while word.count(''):
        word.remove('')
    word = list(map(lambda x: x[::-1], word))
    words.extend(' '.join(word))
print(''.join(words))