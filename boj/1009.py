#bronze 3

import sys
input = sys.stdin.readline

t = int(input())

for x in range(t):
    a, b = map(int, input().split())
    a %= 10
    b %= 4

    d = {1:[1, 1, 1, 1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6, 4, 6],
         5:[5, 5, 5, 5], 6:[6, 6, 6, 6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6],
         9:[9, 1, 9, 1], 0:[10, 10, 10, 10]}

    print(d[a][b-1])
