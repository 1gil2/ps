#silver 3

import sys
input = sys.stdin.readline

n = int(input())

if n%7 == 0 or n%7 == 2:
    print("CY")
else:
    print("SK")