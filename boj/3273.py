#silver 3

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

cnt = 0
left = 0
right = n-1

while left < right:
    temp = arr[left] + arr[right]

    if temp == x:
        cnt += 1
        left += 1
        right -= 1
    elif temp > x:
        right -= 1
    else:
        left += 1

print(cnt)
