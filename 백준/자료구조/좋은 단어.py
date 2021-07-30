N = int(input())
words = [input() for _ in range(N)]

def check(string):
    stack = []
    for i in range(len(string)):
        if stack and stack[-1] :
            if string[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(string[i])
        elif stack == [] :
            stack.append(string[i])

    return 1 if stack == [] else 0

cnt = 0
for word in words:
    cnt += check(word)
print(cnt)