#platinum 5

import sys

input = sys.stdin.readline


def manacher(st, n):
    r = 0
    p = 0
    for i, a in enumerate(st):
        if i <= r:
            A[i] = min(A[2 * p - i], r - i)
        else:
            A[i] = 0

        while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and st[i - A[i] - 1] == st[i + A[i] + 1]:
            A[i] += 1

        if r < i + A[i]:
            r = i + A[i]
            p = i


st = input().rstrip()
le = len(st)
le2 = 2 * le + 1
arr = ['#' for x in range(le2)]

for i, s in enumerate(st):
    arr[2 * i + 1] = s

A = [0 for x in range(le2)]
manacher(arr, le2)

print(max(A))
