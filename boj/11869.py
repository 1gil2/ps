#platnum 4

import sys
input = sys.stdin.readline

n = int(input())
coins = list(map(int, input().split()))

xor = 0
for coin in coins:
    xor ^= coin

if xor:
    print('koosaga')
else:
    print('cubelover')
