#gold 5

import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

print(m - math.gcd(n, m))
