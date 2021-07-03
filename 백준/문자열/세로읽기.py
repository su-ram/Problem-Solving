text = []
max_length = 0
for _ in range(5):
    word = input()
    if len(word) > max_length:
        max_length = len(word)
    text.append(word)

out= ''
for i in range(max_length):
    for j in range(5):
        if i < len(text[j]) and text[j][i] != '':
                out += text[j][i]

print(out)
