#silver 1

import sys
input = sys.stdin.readline

n = int(input())
num = [x for x in range(1, n+1)]
cmd = list(map(int, input().split()))
fac = [0, 1]
for x in range(2, 21):
    fac.append(fac[-1]*x)
