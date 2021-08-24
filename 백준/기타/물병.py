n, k = map(int, input().split())
num = n
def merge(num):
    return bin(num).count('1')

while True :
    cnt = merge(num)
    if cnt > k :
        num += 1
    else:
        print(num - n)
        break