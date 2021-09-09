import sys
input = sys.stdin.readline
nums = set()

for _ in range(int(input())):
    cmd = input().rstrip()
    if len(cmd.split()) == 2 :
        cmd, n = cmd.split()
        n = int(n)

    if cmd == 'add':
        nums.add(n)
    if cmd == 'remove':
        nums.discard(n)
    if cmd == 'check':
        print( 1 if n in nums else 0)
    if cmd == 'toggle':
        if n in nums:
            nums.discard(n)
        else:
            nums.add(n)
    if cmd == 'all':
        nums = set([j for j in range(1, 21)])

    if cmd == 'empty' :
        nums = set()
