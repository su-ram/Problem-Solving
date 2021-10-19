

def solution(string):

    open = ['(', '[']
    close = [')', ']']
    stack = []
    n = 1

    for c in string:
        if c in open:
            stack.append(c)
        elif c in close:
            popped = 0
            while stack and stack[-1] not in open and stack[-1] not in close:
                popped += stack.pop()

            if stack == [] or stack[-1] in close:return False

            if open.index(stack[-1]) == close.index(c):
                if popped:
                    popped *= (close.index(c)+2)
                else:
                    popped = close.index(c) + 2
                stack.pop()
                stack.append(popped)
            else:
                return False

    for c in stack:
        if c in open or c in close:
            return False
    return sum(stack)



print(solution('[(])'))

