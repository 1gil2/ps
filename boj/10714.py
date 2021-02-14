# gold 3

import sys
sys.setrecursionlimit(10**6)


def pl(x):
    return (x + 1) % n


def mi(x):
    return (x + n - 1) % n


def ioi(left, right):
    if mi(left) % n == right:
        return 0

    if cake[mi(left)] > cake[pl(right)]:
        return joi(mi(left), right)

    return joi(left, pl(right))


def joi(left, right):
    if mi(left) == right:
        return 0

    if dp[left][right] != -1:
        return dp[left][right]

    dp[left][right] = max(cake[mi(left)] + ioi(mi(left), right), cake[pl(right)] + ioi(left, pl(right)))
    return dp[left][right]


ans = 0
dp = [[-1 for y in range(2001)] for x in range(2001)]
# dp[x][y] 남아있는 양끝 인덱스가 x, y

n = int(input())
cake = []
for x in range(n):
    cake.append(int(input()))

for x in range(n):
    ans = max(ans, cake[x] + ioi(x, x))

print(ans)
