string = input()
from collections import Counter
counter = list(Counter(list(string)).items())
center = ''
for count in counter:
    if count[1] % 2 == 1 :
        if center == '':
            center = count[0]
        else:
            print("I'm Sorry Hansoo")
            exit(0)
counter = sorted(counter, key=lambda x : x[0])
palindrome = ''
for i in range(len(counter)):
    palindrome += counter[i][0] * (counter[i][1] // 2)
if len(string) % 2 == 1 :
    print(palindrome+center+palindrome[::-1])
else:
    print(palindrome + palindrome[::-1])
