import unittest, math
from collections import deque

'''
1. Please implement your functions that can solve the next 3 questions. 
2. You can choose a language at the bottom of this page
3. Before the test, you should comment out texts of this guidance and next questions.
4. You have to implement functions and test those on this page.
5. Please make your input and test it.
6. Please leave your functions on this page.
'''

'''
Q1> Given a string IP, return whether IP is a valid IPv4 address or not.
A valid IPv4 has a form of “A.B.C.D” with following conditions.
Condition 1: values of A, B, C and D are between 0 and 255. ( 0 <= A, B, C, D <= 255)
Condition 2: A,B,C and D can’t contain leading zeros
examples>
“1.2.3.4” : True
“0.0.0.0” : True
“211.211.211.211” : True
“01.0.0.0: False ( “01” have leading zero)
“00.00.00.00”: False (“00” have leading zero)
“255.255.255.256”: False (256 is out of range)
“15.15.15.15.15” : False
"1.1.1.1.1" : False
“0.0.0” : False
'''


def question1(ipstr: str):
    ips = ipstr.split('.')

    if len(ips) != 4: return False

    for ip in ips:
        if ip.isdigit() is False or (len(ip) > 1 and ip[0] == '0'):
            return False
    try:
        ips = list(map(int, ips))
    except:
        return False

    ips = list(map(lambda x: True if 0 <= x <= 255 else False, ips))

    if False in ips: return False

    return True


'''
Q2> Given values of coins and an amount of money, return the minimum number of coins to make up the given amount of money. If impossible, return -1.
Each coin is provided infinitely.
Example> 
Input: values_of_coins = [1, 3, 10] amount = 0
Output: 0

Input: values_of_coins = [1, 3, 10] amount = 20
Output: 2  (10 * 2 = 20)

Input: values_of_coins = [2, 5, 10] amount = 1
Output: -1 (It’s impossible)

Input: values_of_coins = [1, 4, 5] amount = 14
Output: 3 (4 * 1 + 5 * 2 = 14)

Input: values_of_coins = [1, 5, 10] amount = 101
Output: 11 (1 * 1 + 10 * 10 = 101)

'''


def question2(coins, amount):
    dp = [math.inf] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[-1] if dp[-1] != math.inf else -1


'''
Q3> 
Given an m x n 2D binary grid which represents a map of 1s (land) and 0s (water), 
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
All four edges of the grid are surrounded by water.
- You can use any input data structure that can represent the 2D binary grid.
- Implement the function and test with your inputs.

Example>

Input: grid = [
["0","0","0","1","0"],
["1","1","0","1","0"],
["0","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 2

Input: grid = [
["1","0","0","0","0"],
["0","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
Output: 4

Input: grid = [
["1","0","0","0","1"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["1","0","0","1","1"]
]
Output: 5
'''


def question3(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    groups = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and visited[i][j] is False:

                q = deque([(i, j)])
                check = set([(i, j)])

                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]

                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and (nx, ny) not in check:
                            q.append((nx, ny))
                            check.add((nx, ny))

                for x, y in check:
                    visited[x][y] = True
                groups += 1

    return groups


class QuestionTest(unittest.TestCase):

    def test_q1(self):
        self.assertEqual(question1('12.11.111.1'), True)
        self.assertEqual(question1('heelo.11.111.1'), False)
        self.assertEqual(question1('.11.1'), False)
        self.assertEqual(question1('..19.0.1'), False)
        self.assertEqual(question1('234.234.234.70'), True)
        self.assertEqual(question1('0.0.0.1.1.1'), False)
        self.assertEqual(question1('211....2......1'), False)
        self.assertEqual(question1('12.00.00.78'), False)
        self.assertEqual(question1('0.0.0.0'), True)
        self.assertEqual(question1('0.1.45.290'), False)

    def test_q2(self):
        self.assertEqual(question2([20, 9, 3, 5], 900), 45)
        self.assertEqual(question2([1, 2, 3, 4, 5], 4), 1)
        self.assertEqual(question2([2, 19], 17), -1)
        self.assertEqual(question2([1, 2, 3, 4, 5], 98), 20)
        self.assertEqual(question2([237, 8, 54], 90), -1)
        self.assertEqual(question2([1, 2, 3, 4, 5], 450), 90)
        self.assertEqual(question2([5, 10, 500], 2400), 44)
        self.assertEqual(question2([1, 2], 30), 15)
        self.assertEqual(question2([1, 3, 4], 8), 2)
        self.assertEqual(question2([6, 8, 9], 66), 8)

    def test_q3(self):
        grid = [['0']]
        self.assertEqual(question3(grid), 0)

        grid = [
            ['1', '0', '0'],
            ['0', '1', '0'],
            ['1', '1', '0'],

        ]
        self.assertEqual(question3(grid), 2)

        grid = [
            ['0', '0', '0', '1', '0']
        ]
        self.assertEqual(question3(grid), 1)

        grid = [
            ['1', '1', '1'],
            ['1,', '1', '0'],
            ['1,', '0', '1']
        ]
        self.assertEqual(question3(grid), 2)

        grid = [
            ['0', '0', '1', '0'],
            ['1', '1', '1', '1']
        ]
        self.assertEqual(question3(grid), 1)

        grid = [
            ['0', '0', '1', '0'],
            ['1', '1', '1', '1'],
            ['0', '0', '1', '0'],
            ['1', '1', '1', '1']
        ]
        self.assertEqual(question3(grid), 1)

        grid = [
            ['1', '1', '0', '1'],
            ['1', '0', '1', '0'],
            ['0', '1', '0', '1'],
            ['1', '0', '1', '1'],
            ['0', '0', '0', '1'],
            ['1', '1', '1', '0']

        ]
        self.assertEqual(question3(grid), 7)

        grid = [
            ['0', '0', '1', '0'],
            ['1', '1', '1', '1'],
            ['0', '1', '0', '0'],
            ['1', '1', '1', '1'],
            ['1', '0', '1', '0'],
            ['1', '0', '0', '1'],
            ['1', '0', '1', '1'],
            ['1', '0', '1', '0']
        ]
        self.assertEqual(question3(grid), 2)

        grid = [
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1'],
            ['1', '0', '1', '1'],
            ['1', '1', '0', '1'],
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1']
        ]
        self.assertEqual(question3(grid), 1)

        grid = [
            ['1', '0', '1', '0'],
            ['0', '1', '0', '1'],
            ['1', '0', '1', '0']

        ]
        self.assertEqual(question3(grid), 6)


if __name__ == '__main__':
    unittest.main()


