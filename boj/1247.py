#bronze 3

import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())

    tot = 0
    for i in range(n):
        tot += int(input())

    if tot > 0:
        print('+')
    elif tot < 0:
        print('-')
    else:
        print(0)
