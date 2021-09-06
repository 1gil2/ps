#gold 1

import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

diff = [arr1[x]-arr2[x] for x in range(n)] + [0]

ans = 0
prev = diff[0]

for x in range(1, n+1):
    if prev * diff[x] <= 0:
        ans += abs(prev)
    elif abs(prev) > abs(diff[x]):
        ans += abs(prev - diff[x])

    prev = diff[x]

print(ans)
