string = input()
from itertools import combinations
ordered_string = 'z'
index = list(combinations(range(1, len(string)), 2))

def split(x,y, string):
    return [string[:x], string[x:y], string[y:]]


for x, y in index:
    reversed_string = ''.join(list(map(lambda x : x[::-1], split(x,y,string))))
    if reversed_string < ordered_string:
        ordered_string = reversed_string

print(ordered_string)
