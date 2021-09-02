#gold 2

import sys
input = sys.stdin.readline

n = int(input())

m = n%5

if m == 0 or m == 2:
    print('CY')
else:
    print('SK')
