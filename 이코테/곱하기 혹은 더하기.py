string = list(map(int, list(input())))
init = 0
i = 0
while not init and i < len(string):
    if string[i] > 0 :
        init = string[i]
    i += 1

for j in range(i,len(string)):
    if string[j] == 0 : continue
    init *= string[j]
print(init)