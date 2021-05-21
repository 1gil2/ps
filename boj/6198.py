#gold 5

import sys
input = sys.stdin.readline

n = int(input())
h = []
for x in range(n):
    h.append(int(input()))

ans = 0
stack = []

for x in range(n):

    while stack and stack[-1] <= h[x]:
        stack.pop()

    stack.append(h[x])

    ans += len(stack)-1

print(ans)
