string = input()
answer = ''
for i in string :
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)

