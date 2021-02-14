#bronze 3

import sys

n = int(sys.stdin.readline())
for x in range(n):
    m = int(sys.stdin.readline())
    div = 0
    gpa = 0
    for y in range(m):
        L = sys.stdin.readline().split()
        div += int(L[0])
        gpa += int(L[0])*(float(L[1])*10)
    cgpa = gpa/(10*div)
    print("{:d} {:.1f}".format(div, cgpa))
