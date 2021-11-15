#bronze 5

import sys
input = sys.stdin.readline

temp = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
for x in range(6):
    print(temp[x] - arr[x], end = ' ')
