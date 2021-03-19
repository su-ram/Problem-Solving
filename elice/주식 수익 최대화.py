def maximizeProfit(nums):
    # dp로 푸는 것인가?!!

    dp = [0] * len(nums)
    dp[1] = nums[1] - nums[0] if nums[1] - nums[0] > 0 else 0

    lowest_selling_price = nums[0]

    for i in range(2, len(nums)):

        dp[i] = max(nums[i] - lowest_selling_price, dp[i - 1])

        if nums[i] < lowest_selling_price:
            lowest_selling_price = nums[i]

    return max(dp)


def main():
    print(maximizeProfit([3, 8, 1, 7, 3, 1, 2]))  # 35


if __name__ == "__main__":
    main()