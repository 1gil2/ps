#gold 5

import sys


def mod4(x):
    y = (x//4)*4
    ans = 0
    while x >= y:
        ans ^= y
        y += 1
    return ans


for x in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(mod4(a-1) ^ mod4(b))
