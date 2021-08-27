T = int(input())
prime_digit = {2:[6,2,4,8], 3:[1,3,9,7], 5:[5], 7:[1, 9,3,7]}

def divide(num):
    primes = {2:0, 3:0, 5:0, 7:0}
    for prime in primes.keys():
        while num % prime == 0 :
            primes[prime] += 1
            num = num // prime
    return primes, num
def getlast_digit(prime_divided):
    total_end = 1
    for k, v in prime_divided.items():
        if v :
            end_index = v % (len(prime_digit.get(k)))
            total_end *= prime_digit.get(k)[end_index]
    return total_end if total_end < 10 else int(str(total_end)[-1])

def which_server(a, b):
    prime, noneprime = divide(a)
    prime = dict(map(lambda x : (x[0], x[1] * b), prime.items()))
    end_digit = getlast_digit(prime)
    noneprime, temp = divide(noneprime)
    noneprime = dict(map(lambda x : (x[0], x[1] * b), noneprime.items()))
    end_digit *= getlast_digit(noneprime)
    end_digit = end_digit if end_digit < 10 else int(str(end_digit)[-1])
    print(end_digit if end_digit != 0 else 10)

for _ in range(T):
    a, b = map(int, input().split())
    end = 1
    for __ in range(b):
        end = (end*a) % 10
    if end == 0:
        print(10)
    else:
        print(end)