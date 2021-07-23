#silver 2

import sys
from itertools import permutations
input = sys.stdin.readline


def calc(permu):
    ret = 0
    for x in range(n-1):
        ret += abs(permu[x] - permu[x+1])
    return ret


n = int(input())
nums = list(map(int, input().split()))
ans = -sys.maxsize

permus = permutations(nums, n)
for permu in permus:
    ans = max(ans, calc(permu))

print(ans)
