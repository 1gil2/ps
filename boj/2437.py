#gold 3

import sys
input = sys.stdin.readline

n = int(input())
chus = list(map(int, input().split()))
chus.sort()

total = 0

for chu in chus:
    if total+1 < chu:
        break
    total += chu

print(total+1)
