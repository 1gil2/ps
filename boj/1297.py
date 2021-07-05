#bronze 4

import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

c = (a ** 2 + b ** 2) ** 0.5

x = int((n*a)//c)
y = int((n*b)//c)

print(x, y)
