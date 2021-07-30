#gold 2

import sys

input = sys.stdin.readline


def check(mid):
    cnt = 1
    temp = 0
    for ball in balls:
        temp += ball
        if temp > mid:
            cnt += 1
            temp = ball

    if cnt <= m:
        return True
    return False


def divide(mid, m):
    cnt = 0
    temp = 0
    for idx, ball in enumerate(balls):
        temp += ball

        if temp > mid:
            answer.append(cnt)
            m -= 1
            cnt = 0
            temp = ball
        cnt += 1

        if n - idx == m:
            break

    while m:
        answer.append(cnt)
        cnt = 1
        m -= 1

    return


n, m = map(int, input().split())
balls = list(map(int, input().split()))

left = max(balls)
right = 30000
answer = []

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)
divide(left, m)
print(*answer)
