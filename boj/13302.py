#gold 5

import sys
input = sys.stdin.readline


def go(day, coupon):
    ret = dp[day][coupon]

    if day > n:
        return 0
    if ret != -1:
        return ret
    if non[day]:
        dp[day][coupon] = go(day+1, coupon)
        return dp[day][coupon]

    ret = min(10000 + go(day+1, coupon), 25000 + go(day+3, coupon+1), 37000 + go(day+5, coupon+2))

    if coupon >= 3:
        ret = min(ret, go(day+1, coupon-3))

    dp[day][coupon] = ret
    return ret


n, m = map(int, input().split())
no = list(map(int, input().split()))

non = [0 for x in range(101)]
for x in no:
    non[x] = 1

#dp[x][y] x일 y쿠폰 비용
dp = [[-1 for y in range(111)] for x in range(111)]

print(go(1, 0))
