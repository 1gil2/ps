# gold 4

import sys

input = sys.stdin.readline

n = int(input())
arr = [[0 for x in range(3)] for y in range(n)]
Mdp = [[0 for x in range(3)] for y in range(2)]
mdp = [[0 for x in range(3)] for y in range(2)]
temp = [0 for x in range(3)]

for x in range(n):
    a, b, c = map(int, input().split())
    arr[x][0] = a
    arr[x][1] = b
    arr[x][2] = c

mdp[0][0] = arr[0][0]
mdp[0][1] = arr[0][1]
mdp[0][2] = arr[0][2]

Mdp[0][0] = arr[0][0]
Mdp[0][1] = arr[0][1]
Mdp[0][2] = arr[0][2]

for x in range(1, n):
    Mdp[1][0] = max(Mdp[0][0], Mdp[0][1]) + arr[x][0]
    Mdp[1][1] = max(Mdp[0][0], Mdp[0][1], Mdp[0][2]) + arr[x][1]
    Mdp[1][2] = max(Mdp[0][1], Mdp[0][2]) + arr[x][2]

    mdp[1][0] = min(mdp[0][0], mdp[0][1]) + arr[x][0]
    mdp[1][1] = min(mdp[0][0], mdp[0][1], mdp[0][2]) + arr[x][1]
    mdp[1][2] = min(mdp[0][1], mdp[0][2]) + arr[x][2]

    Mdp[0][0] = Mdp[1][0]
    Mdp[0][1] = Mdp[1][1]
    Mdp[0][2] = Mdp[1][2]

    mdp[0][0] = mdp[1][0]
    mdp[0][1] = mdp[1][1]
    mdp[0][2] = mdp[1][2]

print(max(Mdp[0][0], Mdp[0][1], Mdp[0][2]), min(mdp[0][0], mdp[0][1], mdp[0][2]))
