#bronze 3

import math

for x in range(int(input())):
    n = int(input())
    m = int(math.sqrt(n))
    while True:
        if m*(m+1) <= n:
            print(m)
            break
        m -= 1
