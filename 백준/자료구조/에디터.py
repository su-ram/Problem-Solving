import sys
input = sys.stdin.readline
str = list(input().rstrip())
N = len(str)
M = int(input())
commands = [ input().rstrip().split() for _ in range(M)]
index = len(str)

def execute(str, stack, cmd, char=None):

    if cmd == 'L' and str != []:
        stack.append(str.pop())
    if cmd == 'D' and stack != []:
        str.append(stack.pop())
    if cmd == 'B' and str != []:
        str.pop()
    if cmd == 'P':
        str.append(char)

stack = []
for c in commands:
    index = execute(str=str, stack=stack, cmd=c[0], char= c[1] if len(c) ==2 else None)

print(''.join(str+stack[::-1]))