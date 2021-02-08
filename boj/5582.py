#gold 5
#pypy3

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
M = 0
l1 = len(s1)
l2 = len(s2)

dp = [[0 for y in range(l2+1)] for x in range(l1+1)]

for x in range(l1):
    for y in range(l2):
        if s1[x] == s2[y]:
            dp[x+1][y+1] = dp[x][y] + 1
        else:
            dp[x+1][y+1] = 0
        M = max(M, dp[x+1][y+1])

print(M)
