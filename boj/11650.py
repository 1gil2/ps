#silver 5

import sys

num = []

n = int(input())

for x in range(n):
    num.append(list(map(int, input().split())))

num.sort()

for x in range(n):
    print(num[x][0], num[x][1])
