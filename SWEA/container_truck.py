T=int(input())

def Deliver(container, truck):
    #하나의 트럭에 실을 수 있는 가장 많은 컨테이너
    result = 0

    for i in container:
        if i <= truck :
            result = i
            return result
    if result == 0 :
        return -1


for _ in range(T):
    N, M = map(int, input().split())
    container = []
    truck = []
    container.extend(list(map(int, input().split())))
    truck.extend(list(map(int, input().split())))

    left = sorted(container, reverse=True)
    hap = 0
    for i in truck:
        load = Deliver(left,i)
        if load >=0 :
            left.remove(load)
            hap += load
    print("#%d %d" % (_+1,hap))










