string = input()
answer = ''
for i in string :
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)
#스트링의 특정 문자열을 고칠 순 없다. Cannot assign!!

