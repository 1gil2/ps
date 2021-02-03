#gold 5

import math

N = input()
A = eval('*'.join(input().split()))
M = input()
B = eval('*'.join(input().split()))
gcd = str(math.gcd(A, B))

print(gcd) if len(gcd) < 9 else print(gcd[len(gcd) - 9:len(gcd) + 1])
