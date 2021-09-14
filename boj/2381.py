#gold 4

import sys
input = sys.stdin.readline

n = int(input())

A = []
B = []

for _ in range(n):
    x, y = map(int, input().split())
    A.append(x+y)
    B.append(x-y)

A.sort()
B.sort()

print(max(abs(A[0] - A[-1]), abs(B[0] - B[-1])))
