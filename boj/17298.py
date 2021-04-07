#gold 4

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ans = [-1 for x in range(n)]
stack = [0]
idx = 1

while stack and idx < n:
    while stack and A[stack[-1]] < A[idx]:
        ans[stack[-1]] = A[idx]
        stack.pop()

    stack.append(idx)
    idx += 1

print(" ".join([str(a) for a in ans]))
