earth, sun, moon = map(int, input().split())
e, s, m = 1, 1, 1
num = 1
while True :
    if e == earth and s == sun and m == moon:
        print(num)
        break

    e += 1
    s += 1
    m += 1
    num += 1

    if e > 15 : e = 1
    if s > 28 : s = 1
    if m > 19 : m = 1

