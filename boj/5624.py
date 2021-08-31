#gold 4

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

visit = [False for x in range(400001)]

cnt = 0

for x in range(n):
    for y in range(x):
        if visit[arr[x] - arr[y] + 200000]:
            cnt += 1
            break

    for y in range(x+1):
        visit[arr[x] + arr[y] + 200000] = True

print(cnt)
