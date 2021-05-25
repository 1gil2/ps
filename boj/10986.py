#gold 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

pasum = [0]

mod = [0 for x in range(m)]
mod[0] += 1

for x in range(n):
    temp = (pasum[-1] + a[x])%m
    pasum.append(temp)
    mod[temp] += 1

ans = 0
for mo in mod:
    ans += mo*(mo-1)//2

print(ans)
