#silver 5

import sys
from itertools import permutations
input = sys.stdin.readline


def trans(temp):
    ans = ''
    for x in temp:
        ans += str(x)
    return ans


n = int(input())
k = int(input())
num = []
for x in range(n):
    num.append(int(input()))

s = set()
per = permutations(num, k)
for x in per:
    s.add(trans(x))

print(len(s))
