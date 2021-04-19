#silver 4

import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
oils = list(map(int, input().split()))

temp = sys.maxsize
ans = 0

for idx, d in enumerate(dist):
    temp = min(temp, oils[idx])
    ans += temp * d

print(ans)
