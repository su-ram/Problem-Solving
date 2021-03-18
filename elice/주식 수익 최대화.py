def maximizeProfit(nums):

    buying = nums[0]
    selling = -1
    next_buying = -1

    for n in nums:

        if n > selling:
            selling = n

            if next_buying != -1:
                    buying = next_buying
                    next_buying = -1

        if n < buying:
            next_buying = n

    return selling - buying

def main():

    print(maximizeProfit([7,6,5,4,3]))


if __name__ == "__main__":
    main()