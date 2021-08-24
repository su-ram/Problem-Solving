colors = {
    'black' : '0',
    'brown' : '1',
    'red' : '2',
    'orange' : '3',
    'yellow' : '4',
    'green' : '5',
    'blue' : '6',
    'violet' : '7',
    'grey' : '8',
    'white':'9'
}

x, y, z = [ input() for _ in range(3)]
num = colors.get(x) + colors.get(y) + '0' * int(colors.get(z))
print(num)
