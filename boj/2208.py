#gold 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
juwel = [int(input()) for x in range(n)]

psum = [0 for x in range(n+1)]
psum[1] = juwel[0]

for x in range(1, n):
    psum[x+1] = psum[x] + juwel[x]

ans = 0
psum2 = 0

for x in range(m-1, n):
    psum2 = min(psum2, psum[x-m+1])
    ans = max(ans, psum[x+1] - psum2)

print(ans)
