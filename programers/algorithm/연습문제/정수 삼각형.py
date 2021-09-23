#level 3


def solution(triangle):
    lv = len(triangle)
    for x in range(1, lv):
        for y in range(x + 1):
            if y == 0:
                triangle[x][y] += triangle[x - 1][y]
            elif x == y:
                triangle[x][y] += triangle[x - 1][y - 1]
            else:
                triangle[x][y] += max(triangle[x - 1][y], triangle[x - 1][y - 1])

    return max(triangle[-1])
