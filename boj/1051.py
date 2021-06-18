#silver 3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = []
for x in range(n):
    arr = []
    temp = input().rstrip()
    for x in temp:
        arr.append(int(x))
    table.append(arr)

gap = min(n, m)
ans = 0

for x in range(n):
    for y in range(m):
        for k in range(gap):
            if 0 <= x+k < n and 0 <= y+k < m:
                if table[x][y] == table[x][y+k] == table[x+k][y] == table[x+k][y+k]:
                    ans = max(ans, k)
            else:
                break

print((ans + 1) ** 2)
