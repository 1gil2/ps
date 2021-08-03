#gold 5

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

ans = sys.maxsize
answer = [left, right]

while left < right:
    temp = arr[left] + arr[right]

    if ans > abs(temp):
        ans = abs(temp)
        answer = [arr[left], arr[right]]

    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    else:
        break

print(*answer)
