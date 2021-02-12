#gold 5

import sys
sys.setrecursionlimit(10**6)

def back_lcs(a, b):
    global ans
    if a < 0 or b < 0:
        return
    if s1[a] == s2[b]:
        ans += s1[a]
        back_lcs(a-1, b-1)
    else:
        if a == 0:
            for x in range(b+1):
                if s2[x] == s1[0]:
                    ans += s1[0]
                    return
            return

        if b == 0:
            for x in range(a+1):
                if s2[0] == s1[x]:
                    ans += s2[0]
                    return
            return

        if dp[a-1][b] >= dp[a][b-1]:
            back_lcs(a-1, b)
        else:
            back_lcs(a, b-1)


s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

ans = ''

dp = [[0 for y in range(1001)] for x in range(1001)]

flag = 0
for x in range(l1):
    if s2[0] == s1[x]:
        flag = 1
    dp[x][0] = flag
dp[l1][0] = flag

flag = 0
for x in range(l2):
    if s2[x] == s1[0]:
        flag = 1
    dp[0][x] = flag
dp[0][l2] = flag

for x in range(1, l1):
    for y in range(1, l2):
        if s1[x] == s2[y]:
            dp[x][y] = dp[x-1][y-1] + 1
        else:
            dp[x][y] = max(dp[x-1][y-1], dp[x-1][y], dp[x][y-1])

print(dp[l1-1][l2-1])
back_lcs(l1-1, l2-1)
print(ans[::-1])
