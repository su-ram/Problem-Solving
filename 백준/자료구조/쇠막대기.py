brackets = list(input())
stack = []
open = [0] * len(brackets)

for i in range(len(brackets)):

    if brackets[i] == '(':
        stack.append(i)
        continue
    if brackets[i] == ')':

        if stack != []:
            stack.pop()
        if brackets[i-1] == '(':
            for j in stack:
                open[j] += 1


print(sum([ i + 1 for i in open if i > 0]))