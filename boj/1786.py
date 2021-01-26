#gold 1

import sys
sys.setrecursionlimit(10**6)

T = input()
P = input()
lt = len(T)
lp = len(P)

ans = []
cnt = 0

Pi = [0 for x in range(lp)]
j = 0
for i in range(1, lp):
    while j > 0 and P[i] != P[j]:
        j = Pi[j-1]
    if P[i] == P[j]:
        j += 1
        Pi[i] = j

j = 0
for i in range(lt):
    while j > 0 and T[i] != P[j]:
        j = Pi[j-1]
    if T[i] == P[j]:
        if j == lp-1:
            ans.append(i-lp+2)
            cnt += 1
            j = Pi[j]
        else:
            j += 1

print(cnt)
for x in ans:
    print(x, end=' ')
