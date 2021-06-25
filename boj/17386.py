#gold 3

import sys

input = sys.stdin.readline


def ccw(p1, p2, p3):
    ret = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p1[1] * p2[0] - p2[1] * p3[0] - p3[1] * p1[0]
    if ret > 0:
        return 1
    elif ret < 0:
        return -1
    else:
        return 0


x1, y1, x2, y2 = map(int, input().split())
if (x1, y1) > (x2, y2):
    x1, y1, x2, y2 = x2, y2, x1, y1

A = (x1, y1)
B = (x2, y2)

x3, y3, x4, y4 = map(int, input().split())
if (x3, y3) > (x4, y4):
    x3, y3, x4, y4 = x4, y4, x3, y3

C = (x3, y3)
D = (x4, y4)

check1 = ccw(A, B, C) * ccw(A, B, D)
check2 = ccw(C, D, A) * ccw(C, D, B)

if A == C or A == D or B == C or B == D:
    print(1)
elif check1 == 0 and check2 == 0:
    if A <= D and C <= B:
        print(1)
    else:
        print(0)
elif check1 <= 0 and check2 <= 0:
    print(1)
else:
    print(0)
