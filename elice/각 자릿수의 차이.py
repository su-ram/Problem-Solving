def diffDigit(a, b) :
    '''
    a, b의 서로 다른 자리수의 개수를 반환한다
    '''
    longer = max(a,b)
    shorter = min(a,b)
    longer = str(longer)
    shorter = str(shorter)
    offset = len(longer) - len(shorter)
    cnt = offset

    for i in range(len(shorter)):

        if shorter[i] != longer[(offset+i)]:
            cnt += 1

    return cnt

def main():
    '''
    Do not change this code
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()
