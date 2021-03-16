
def attending(meetingList):

    meetingList.sort()
    cnt = 1
    curr = meetingList[0]

    for i in range(len(meetingList)):

        meeting = meetingList[i]

        if meeting[0] >= curr[0] and meeting[1] < curr[1]:
            curr = meeting

        if meeting[0] >= curr[1]:
            curr = meeting
            cnt += 1

    return cnt


def main():

    n = int(input())
    meetingList = []

    for i in range(n):
        data = [int(x) for x in input().split()]
        meetingList.append((data[0], data[1]))

    print(attending(meetingList))

if __name__ == "__main__":
    main()
