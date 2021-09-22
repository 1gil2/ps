#gold 2

import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


g = int(input())
p = int(input())

planes = [int(input()) for x in range(p)]
parent = [x for x in range(g+1)]

answer = 0
for plane in planes:
    docking = find(plane)

    if docking == 0:
        break
    parent[docking] = parent[docking-1]
    answer += 1

print(answer)
