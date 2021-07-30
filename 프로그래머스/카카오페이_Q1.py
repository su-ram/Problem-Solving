



def cal(money, minratio, maxratio, ranksize, threshold):

    origin_money = money

    if len(str(money)) > 2:
        money /= 100
        money = int(money)
        money *= 100

    if money < threshold:
        return
    plus = (money - threshold) // ranksize
    tax_ratio = maxratio if minratio + plus >=maxratio else plus + minratio
    return int(origin_money - (tax_ratio * money / 100))


def solution(money, minratio, maxratio, ranksize, threshold, months):
    for i in range(months):
        money = cal(money, minratio, maxratio, ranksize, threshold)
        print(money)

solution(1000000000, 50, 99, 100000,0, 6)