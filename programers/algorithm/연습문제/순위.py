#level 3


def solution(n, results):
    ans = 0
    inf = 987654321
    table = [[inf for x1 in range(n + 1)] for x2 in range(n + 1)]
    rank = [0 for x in range(n + 1)]

    for box in results:
        table[box[0]][box[1]] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if table[i][j] != inf and i != j:
                rank[i] += 1
                rank[j] += 1

    for i in range(1, n + 1):
        if rank[i] == n - 1:
            ans += 1

    return ans
