#silver 3

import sys
input = sys.stdin.readline

x, y = map(int, input().split())

temp = (100 * y) // x

left = 0
right = 1000000000

if temp >= 99:
    print(-1)
    sys.exit()

while left <= right:
    mid = (left + right)//2
    tx = x + mid
    ty = y + mid

    if (100 * ty) // tx > temp:
        right = mid - 1
    else:
        left = mid + 1

print(right+1)
