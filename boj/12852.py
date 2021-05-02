#silver 1

from collections import deque

n = int(input())

dp = [1000001 for x in range(n + 1)]
dp[n] = 0

dq = deque()
dq.append((0, n))

while dq:
    cnt, k = dq.popleft()

    if k < 0:
        continue

    if k % 3 == 0:
        if dp[k // 3] > cnt + 1:
            dp[k // 3] = cnt + 1
            dq.append((cnt + 1, k // 3))

    if k % 2 == 0:
        if dp[k // 2] > cnt + 1:
            dp[k // 2] = cnt + 1
            dq.append((cnt + 1, k // 2))

    if dp[k - 1] > cnt + 1:
        dp[k - 1] = cnt + 1
        dq.append((cnt + 1, k - 1))

ans = dp[1]
trace = [1]
s = 1
while ans:
    if s * 3 < n + 1 and dp[s * 3] == ans - 1:
        ans -= 1
        s *= 3
        trace.append(s)
        continue
    if s * 2 < n + 1 and dp[s * 2] == ans - 1:
        ans -= 1
        s *= 2
        trace.append(s)
        continue
    if s < n and dp[s + 1] == ans - 1:
        ans -= 1
        s += 1
        trace.append(s)

print(dp[1])
for x in trace[::-1]:
    print(x, end=' ')
