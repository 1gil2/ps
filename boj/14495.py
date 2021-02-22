#silver 3

import sys

n = int(sys.stdin.readline())

dp = [0, 1, 1, 1]
for x in range(n-3):
    dp.append(dp[-1]+dp[-3])

print(dp[-1])
