#silver 4

import sys
input = sys.stdin.readline

m = int(input())
stone = list(map(int, input().split()))
k = int(input())
total = sum(stone)

bi = [[0 for y in range(total+1)] for x in range(total+1)]
for x in range(total+1):
    bi[x][0] = 1
    bi[x][x] = 1

for x in range(2, total+1):
    for y in range(1, x):
        bi[x][y] = bi[x-1][y-1] + bi[x-1][y]

head = 0
for x in range(m):
    if stone[x] >= k:
        head += bi[stone[x]][k]

head /= bi[total][k]
print(head)
