#gold 5

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

diff = []
for x in range(n-1):
    diff.append(sensor[x+1] - sensor[x])

diff.sort()

ans = 0
for x in range(n-k):
    ans += diff[x]

print(ans)
