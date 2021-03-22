#silver 1

import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d, e, f = map(int, input().split())

m1 = min(a, b, c, d, e, f)
m2 = min(a+b, b+f, f+e, e+a, a+d, d+f, f+c, c+a, b+d, d+e, e+c, c+b)
m3 = min(a+b+c, a+b+d, a+e+d, a+e+c, e+f+d, e+c+f, b+f+d, b+f+c)

if n == 1:
    print(a+b+c+d+e+f-max(a,b,c,d,e,f))
else:
    total = 5*n*n
    p3 = 4
    p2 = 4* (2*n-3)
    p1 = total - 3*p3 - 2*p2
    print(p3*m3 + p2*m2 + p1*m1)
