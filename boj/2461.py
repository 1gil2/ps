#gold 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

power = []

for i in range(n):
    ban = map(int, input().split())
    for b in ban:
        power.append((b, i))

power.sort()

visit = [0 for x in range(n)]

ans = sys.maxsize
cnt = 0

left = 0
for right in range(n * m):
    if visit[power[right][1]] == 0:
        cnt += 1
    visit[power[right][1]] += 1

    while cnt == n:
        ans = min(ans, power[right][0] - power[left][0])
        visit[power[left][1]] -= 1
        if visit[power[left][1]] == 0:
            cnt -= 1
        left += 1

print(ans)
