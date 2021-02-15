#bronze 1

import sys

for t in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    team = [[0, 0] for x in range(n)]
    for x in range(m):
        a, b, c, d = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        team[a][0] += c
        team[a][1] += d
        team[b][0] += d
        team[b][1] += c
    pytha = [0 for x in range(n)]
    for x in range(n):
        if team[x][0] == 0 and team[x][1] == 0:
            pytha[x] = 0
            continue
        pytha[x] = int(1000*(team[x][0]*team[x][0])/(team[x][0]*team[x][0]+team[x][1]*team[x][1]))
    print(max(pytha))
    print(min(pytha))
