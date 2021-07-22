#gold 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rides = list(map(int, input().split()))

if n < m:
    print(n)
    sys.exit(0)

left = 0
right = 30 * n
time = 0

while left <= right:
    mid = (left + right) // 2

    #1초에 다 태우기
    child = m

    for x in range(m):
        child += (mid // rides[x])

    if child >= n:
        time = mid
        right = mid - 1
    else:
        left = mid + 1

cnt = m
for x in range(m):
    cnt += (time - 1) // rides[x]

for x in range(m):
    if time % rides[x] == 0:
        cnt += 1
    if cnt == n:
        print(x+1)
        break
