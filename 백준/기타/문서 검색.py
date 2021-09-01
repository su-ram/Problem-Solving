doc = input()
word = input()
start = 0
cnt = 0
while doc.count(word, start):
    cnt += 1
    start = doc.index(word, start) + len(word)
print(cnt)