T = int(input())


# def getprimes(num):
#     origin = num
#     add = 0
#
#     primes = {2: 0, 3: 0, 5: 0, 7: 0}
#     for prime in primes.keys():
#         while num % prime == 0 :
#             num = num // prime
#             primes[prime] = primes.get(prime) + 1
#
#     if num != 1:
#         temp = 1
#
#         for k, v in primes.items():
#             temp *= k ** v
#         for s in str(num):
#             temp *= int(s)
#         if temp != origin:
#             return -1
#         add = len(str(num))
#
#     if 0 < primes.get(2) < 4 :
#         primes[2] = 1
#     elif primes.get(2) > 3 :
#         primes[2] = (primes.get(2)//3) + 1 if primes.get(2) % 3 else (primes.get(2)//3)
#
#     if 0 < primes.get(3) < 3 :
#         primes[3] = 1
#     elif primes.get(3) > 2 :
#         primes[3] = (primes.get(3)//2) + 1 if primes.get(3) % 2 else (primes.get(3)//2)
#
#
#
#     return sum(primes.values()) + add
#
# for _ in range(T):
#     print(getprimes(int(input())))

result = []
div = [i for i in range(9, 1, -1)]

for _ in range(T):
    num = int(input())
    if num == 1 :
        result.append(1)
    else:
        cnt = 0
        c = 0
        while True:
            if cnt == 8 :
                result.append(-1)
                break
            if num == 1 :
                result.append(c)
                break
            cnt = 0
            for i in range(8):
                if num % div[i] == 0 :
                    num = num//div[i]
                    c += 1
                    break
                else:
                    cnt += 1
for i in range(T):
    print(result[i])
