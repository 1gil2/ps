#platinum 4

import sys
input = sys.stdin.readline

n = int(input())
stone = list(map(int, input().split()))

xor = 0
for s in stone:
    xor ^= s

if xor:
    print('koosaga')
else:
    print('cubelover')
