#silver 2

import sys

input = sys.stdin.readline


def change(a, b):
    for x in range(a, a + 3):
        for y in range(b, b + 3):
            arr1[x][y] = 1 - arr1[x][y]


n, m = map(int, input().split())

arr1 = [list(map(int, input().rstrip())) for x in range(n)]
arr2 = [list(map(int, input().rstrip())) for x in range(n)]

cnt = 0
for x in range(n - 2):
    for y in range(m - 2):
        if arr1[x][y] != arr2[x][y]:
            change(x, y)
            cnt += 1

if arr1 == arr2:
    print(cnt)
else:
    print(-1)
