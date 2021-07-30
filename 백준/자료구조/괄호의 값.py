brackets = list(input())
stack = []

for b in brackets:

    if b == ')':
        prev = 0
        while stack != []:
            top = stack.pop()
            if top == '(':
                if prev == 0:
                    stack.append(2)
                else:
                    stack.append(2*prev)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                prev += top

    elif b == ']':
        prev = 0
        while stack != []:
            top = stack.pop()
            if top == '[':
                if prev == 0:
                    stack.append(3)
                else:
                    stack.append(3*prev)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                prev += top

    else:
        stack.append(b)

total = 0
for s in stack :
    if s in ['(', '[']:
        print(0)
        exit(0)
    else:
        total += s
print(total)