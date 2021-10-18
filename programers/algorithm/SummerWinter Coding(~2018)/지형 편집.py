#level 4


def solution(land, P, Q):
    mine = []
    for l in land:
        mine += l

    mine.sort()

    n = len(mine)
    cost = (sum(mine) - mine[0] * n) * Q
    answer = min(cost, sum(mine) * Q)

    for x in range(1, n):
        diff = mine[x] - mine[x - 1]
        if diff:
            cost += P * x * diff - Q * (n - x) * diff

            answer = min(answer, cost)

    return answer
