# gold 5

import sys
from itertools import combinations

input = sys.stdin.readline


def check(word):
    mo_cnt = 0
    ja_cnt = 0
    for x in range(l):
        if word[x] in mo:
            mo_cnt += 1
        else:
            ja_cnt += 1
    if mo_cnt >= 1 and ja_cnt >= 2:
        return True
    return False


l, c = map(int, input().split())
item = list(map(str, input().split()))
item.sort()
mo = ['a', 'e', 'i', 'o', 'u']

words = list(combinations(item, l))

for word in words:
    if check(word):
        print(''.join(word))
