#gold 3

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

counter = Counter(a)
temp = [(x, counter[x]) for x in a]

answer = [-1 for x in range(n)]
stack = []

for x in range(n):
    while stack and temp[stack[-1]][1] < temp[x][1]:
        idx = stack.pop()
        answer[idx] = temp[x][0]

    stack.append(x)

print(' '.join([str(x) for x in answer]))
