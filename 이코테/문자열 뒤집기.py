string = list(input())
string = list(map(int, string))
prev = not string[0]
sub= [0,0]
for i in string :
    if i != prev:
        sub[i] +=1
        prev = i
print(min(sub))