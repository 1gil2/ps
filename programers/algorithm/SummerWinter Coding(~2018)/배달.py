#level 2

import sys


def solution(N, road, K):
    table = [[sys.maxsize for y in range(N + 1)] for x in range(N + 1)]
    for x in range(N + 1):
        table[x][x] = 0

    for a, b, c in road:
        table[a][b] = min(table[a][b], c)
        table[b][a] = min(table[b][a], c)

    for k in range(1, N + 1):
        for x in range(1, N + 1):
            for y in range(1, N + 1):
                if table[x][y] > table[x][k] + table[k][y]:
                    table[x][y] = table[x][k] + table[k][y]

    answer = 0
    for x in range(1, N + 1):
        if table[1][x] <= K:
            answer += 1

    return answer
