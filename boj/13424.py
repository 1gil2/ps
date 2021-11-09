#gold 4

import sys
input = sys.stdin.readline
inf = sys.maxsize

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    table = [[inf for y in range(n+1)] for x in range(n+1)]

    for x in range(n+1):
        table[x][x] = 0

    for x in range(m):
        a, b, c = map(int, input().split())
        table[a][b] = c
        table[b][a] = c

    k = int(input())
    friends = list(map(int, input().split()))

    for z in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                temp = table[x][z] + table[z][y]
                if table[x][y] > temp:
                    table[x][y] = temp

    dist = inf
    ans = 0
    for room in range(1, n+1):
        temp = 0
        for friend in friends:
            temp += table[friend][room]

        if dist > temp:
            dist = temp
            ans = room

    print(ans)
