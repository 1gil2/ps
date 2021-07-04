#silver 5

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

num = []
for x in range(1, 51):
    temp = [x for i in range(x)]
    num.extend(temp)

print(sum(num[a-1:b]))
