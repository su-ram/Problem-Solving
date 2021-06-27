expression = input()
splitted_exp= expression.split('-')
total = 0

for n in splitted_exp[0].split('+'):
    total += int(n)

for exp in splitted_exp[1:]:

    for n in exp.split('+'):
        total -= int(n)

print(total)