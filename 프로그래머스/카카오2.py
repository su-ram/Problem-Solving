import math

def change(n, k):
    new = []
    while n :
        new.append(str(n%k))
        n = n // k
    new = new[::-1]
    return ''.join(new)

def isprime(n):
    array = [True for i in range(n+1)]
    array[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

def solution(n, k):
    answer = 0
    changed = change(n,k)
    primes = []
    maxprime = -1
    for num in changed.split('0'):
        if num != '':
            primes.append(num)
            maxprime = max(maxprime, int(num))
    length = len(changed)
    if len(primes) == 1:
        for i in range(2,int(math.sqrt(int(primes[0])))+1):
            if int(primes[0]) % i == 0 :
                return 1
        return 0
    start = 0
    check = isprime(maxprime)
    for p in primes:
        index = changed.index(p, start)
        last = index + len(p)
        start = index + len(p)
        if not check[int(p)]: continue
        if index - 1 >= 0 and last < length:
            if changed[index-1] == '0' and changed[last] == '0' :
                answer += 1
                continue
        if last + 1 < length:
            if changed[last] == '0':
                answer += 1
                continue
        if index - 1 >= 0:
            if changed[index-1] == '0':
                answer += 1
                continue
    return answer



n = 9999999
k =10
print(solution(n,k))