#gold 4

import sys
input = sys.stdin.readline


def bellman():
    global flag

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for wei, vec in adj[y]:
                if dist[vec] > wei + dist[y]:
                    dist[vec] = wei + dist[y]
                    if x == n:
                        flag = False


t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    dist = [100000007 for x in range(n + 1)]
    adj = [[] for x in range(n + 1)]
    for x in range(m):
        s, e, t = map(int, input().split())
        adj[s].append([t, e])
        adj[e].append([t, s])

    for x in range(w):
        s, e, t = map(int, input().split())
        adj[s].append([-t, e])

    flag = True
    bellman()

    if flag:
        print("NO")
    else:
        print("YES")
