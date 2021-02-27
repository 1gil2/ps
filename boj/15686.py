#gold 5

from itertools import combinations
import math


def calc(chicken):
    chic_dist = 0
    for h in home:
        temp = math.inf
        for c in chicken:
            temp = min(temp, abs(h[0]-c[0])+abs(h[1]-c[1]))
        chic_dist += temp
    return chic_dist


n, m = map(int, input().split())
town = [list(map(int, input().split())) for x in range(n)]

home = []
chic = []
ans = math.inf

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            home.append([i, j])
        if town[i][j] == 2:
            chic.append([i, j])

chic_combi = list(combinations(chic, m))

for x in chic_combi:
    ans = min(ans, calc(x))

print(ans)
