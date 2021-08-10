#platinum 5
#pypy3

import sys

input = sys.stdin.readline


def ccw(p1, p2, p3):
    ret = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])
    if ret > 0:
        return 1
    elif ret < 0:
        return -1
    else:
        return 0


def check(line1, line2):
    p1 = (line1[0], line1[1])
    p2 = (line1[2], line1[3])
    p3 = (line2[0], line2[1])
    p4 = (line2[2], line2[3])

    ccw1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    ccw2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    if ccw1 <= 0 and ccw2 <= 0:
        if (p1[0] > p3[0] and p1[0] > p4[0] and p2[0] > p3[0] and p2[0] > p4[0]) or (
                p1[0] < p3[0] and p1[0] < p4[0] and p2[0] < p3[0] and p2[0] < p4[0]):
            return False
        elif ((p1[1] > p3[1] and p1[1] > p4[1] and p2[1] > p3[1] and p2[1] > p4[1])) or (
        (p1[1] < p3[1] and p1[1] < p4[1] and p2[1] < p3[1] and p2[1] < p4[1])):
            return False
        else:
            return True
    return False


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n = int(input())
parent = [x for x in range(n)]
lines = [list(map(int, input().split())) for x in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        if check(lines[i], lines[j]):
            union(i, j)

cnt = 0
result = [0 for x in range(n)]
for x in range(n):
    if x == parent[x]:
        cnt += 1
    result[find(x)] += 1

print(cnt)
print(max(result))

