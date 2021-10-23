#bronze 3

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
y = 0
m = 0
for a in arr:
    y += a//30 * 10 + 10
    m += a//60 * 15 + 15

if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y M', y)
