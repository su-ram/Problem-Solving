
def plus_One_nTimes(n):
#1을 n번 더하기.
    if n == 0: return 0
    return 1 + plus_One_nTimes(n-1)

def factorial(num):
    
    # 반복문
    # x = 1
    # for each in range(1, num + 1):
    #         x = x * each
    # return x

    #recursion
    if num <= 1: return 1
    return num * factorial(num-1)

def main():
    print(factorial(50000)) # should return 120

if __name__ == "__main__":
    main()