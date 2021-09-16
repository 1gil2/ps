#silver 1

import sys
input = sys.stdin.readline

L, R = input().split()
leL = len(L)
leR = len(R)

ans = 0

if leL != leR:
    print(ans)
else:
    for i in range(leL):
        if L[i] != R[i]:
            break
        else:
            if L[i] =='8':
                ans += 1

    print(ans)
