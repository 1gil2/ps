#platinum 4

import sys
input = sys.stdin.readline

n = int(input())
stone = list(map(int, input().split()))

xor = 0
for s in stone:
    xor ^= s

if xor:
    cnt = 0
    for s in stone:
        if xor ^ s < s+1:
            cnt += 1
    print(cnt)
else:
    print(0)
