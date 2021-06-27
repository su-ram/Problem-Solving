n = input()
array = list(n)
array = sorted(array, key=lambda x : int(x), reverse=True)
print(''.join(array))