#gold 3

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def pre_order(in_i, in_j, post_i, post_j):
    if in_i > in_j or post_i > post_j:
        return

    root = post_order[post_j]
    print(root, end=" ")

    left = idx[root] - in_i
    right = in_j - idx[root]

    pre_order(in_i, in_i + left - 1, post_i, post_i + left - 1)
    pre_order(in_j - right + 1, in_j, post_j - right, post_j - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0 for x in range(n + 1)]

for i in range(n):
    idx[in_order[i]] = i

pre_order(0, n - 1, 0, n - 1)
