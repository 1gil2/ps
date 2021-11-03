#platinum 3

import sys

input = sys.stdin.readline
inf = sys.maxsize


def calc(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def dc(s, e):
    if s == e:
        return inf

    if s + 1 == e:
        return calc(points[s], points[e])

    m = (s + e) // 2
    answer = min(dc(s, m), dc(m, e))

    temp = []
    for x in range(s, e + 1):
        if (points[m][0] - points[x][0]) ** 2 < answer:
            temp.append(points[x])

    temp.sort(key=lambda x: x[1])
    le = len(temp)
    for x in range(le - 1):
        for y in range(x + 1, le):
            if (temp[x][1] - temp[y][1]) ** 2 < answer:
                dist = calc(temp[x], temp[y])
                answer = min(answer, dist)
            else:
                break

    return answer


n = int(input())
points = [tuple(map(int, input().split())) for x in range(n)]
points.sort()

print(dc(0, n - 1))
