def isSame(sub_str1, str2):

    for a, b in zip(sub_str1, str2):
        if a != b:
            return False

    return True

def main():

    str1 = list(input())
    str2 = list(input())

    dp = [0] * (len(list(str1)) + 1)

    for i in range(len(str2) - 1, len(str1)):

        if str1[i] == str2[-1] and isSame(str1[i + 1 - len(str2):i + 1], str2):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    print(max(dp))

if __name__ == "__main__":
    main()