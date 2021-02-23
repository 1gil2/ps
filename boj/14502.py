#gold 5

from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def cnt(A):
    ans = 0
    for x in range(n):
        for y in range(m):
            if A[x][y] == 0:
                ans += 1
    return ans


def bfs(A, V):
    dq = deque(V)

    while dq:
        a = dq.popleft()

        for i in range(4):
            x = a[0] + dx[i]
            y = a[1] + dy[i]

            if 0 <= x < n and 0 <= y < m and A[x][y] == 0:
                A[x][y] = 2
                dq.append([x, y])

    return cnt(A)


n, m = map(int, input().split())
M = 0
virus = []
table = [list(map(int, input().split())) for x in range(n)]
combi = list(combinations(range(n * m), 3))

for x in range(n):
    for y in range(m):
        if table[x][y] == 2:
            virus.append([x, y])

for t in combi:
    x1 = t[0] % n
    y1 = t[0] // n
    x2 = t[1] % n
    y2 = t[1] // n
    x3 = t[2] % n
    y3 = t[2] // n
    if table[x1][y1] == 0 and table[x2][y2] == 0 and table[x3][y3] == 0:
        temp = deepcopy(table)
        V = deepcopy(virus)
        temp[x1][y1] = 1
        temp[x2][y2] = 1
        temp[x3][y3] = 1
        M = max(M, bfs(temp, V))

print(M)