s = int(input())
dp = [0]
index = 1
while True :
    if dp[-1] > s : break
    dp.append(dp[-1] +index)
    index += 1
print(len(dp)-2)