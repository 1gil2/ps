#level 3


def solution(m, n, puddles):
    table = [[0 for x in range(m + 1)] for y in range(n + 1)]
    table[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                continue
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[-1][-1] % 1000000007
