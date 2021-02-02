#bronze 3

import sys

for x in range(3):
    cnt = 0
    for y in map(int, sys.stdin.readline().split()):
        cnt += y
    if cnt == 1:
        print("C")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("A")
    elif cnt == 4:
        print("E")
    else:
        print("D")
