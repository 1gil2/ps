#gold 2
#pypy3

import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []

for x in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum1 = dict()
sum2 = dict()

for a in A:
    for b in B:
        if not sum1.get(a+b):
            sum1[a+b] = 1
        else:
            sum1[a+b] += 1

cnt = 0
for c in C:
    for d in D:
        if sum1.get(-c-d):
            cnt += sum1[-c-d]

print(cnt)
