#gold 4

import sys
input = sys.stdin.readline


def solve(x, y, z):
    if x == 0 and y == 0 and z == 0:
        return 0

    if dp[x][y][z] != -1:
        return dp[x][y][z]

    ret = sys.maxsize
    ret = min(ret, solve(max(0, x-9), max(0, y-3), max(0, z-1)) + 1)
    ret = min(ret, solve(max(0, x-9), max(0, y-1), max(0, z-3)) + 1)
    ret = min(ret, solve(max(0, x-3), max(0, y-1), max(0, z-9)) + 1)
    ret = min(ret, solve(max(0, x-3), max(0, y-9), max(0, z-1)) + 1)
    ret = min(ret, solve(max(0, x-1), max(0, y-3), max(0, z-9)) + 1)
    ret = min(ret, solve(max(0, x-1), max(0, y-9), max(0, z-3)) + 1)

    dp[x][y][z] = ret
    return ret


n = int(input())
dp = [[[-1 for z in range(61)] for y in range(61)] for x in range(61)]
#dp[x][y][z] 체력 x, y, z 남은애들 죽이는 공격 횟수
arr = [0, 0, 0]
temp = list(map(int, input().split()))
for x in range(n):
    arr[x] = temp[x]

print(solve(arr[0], arr[1], arr[2]))
