#silver 1

import math

def ac(n):
    m = int(math.sqrt(n))
    if n == m*m:
        return 2*m-1
    if n <= m*(m+1):
        return 2*m
    return 2*m+1

for t in range(int(input())):
    x, y = map(int, input().split())
    print(ac(y-x))
