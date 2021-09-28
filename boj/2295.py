#gold 4

import sys
input = sys.stdin.readline

n = int(input())
u = [int(input()) for x in range(n)]
u.sort()

# a + b
A = []
# d - c
B = []

for x in range(n):
    for y in range(n):
        A.append(u[x] + u[y])
        B.append((u[x] - u[y], u[x]))

A.sort()
B.sort()

ans = 0
a = 0
b = 0
la = len(A)
lb = len(B)
while a < la and b < lb:
    if A[a] > B[b][0]:
        b += 1
    elif A[a] < B[b][0]:
        a += 1
    else:
        ans = max(ans, B[b][1])
        a += 1
        b += 1

print(ans)
