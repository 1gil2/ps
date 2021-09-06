#gold 4

import sys

input = sys.stdin.readline


def check(mid):
    cnt = 1
    M = arr[0]
    m = arr[0]

    for x in range(1, n):
        M = max(M, arr[x])
        m = min(m, arr[x])
        if M - m > mid:
            cnt += 1
            M = arr[x]
            m = arr[x]

    return cnt


n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 10000

while left <= right:
    mid = (left + right) // 2

    if check(mid) > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)
