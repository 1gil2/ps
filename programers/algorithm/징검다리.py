#level 4

import math


def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    l, r = 0, distance
    lr = len(rocks)

    while l <= r:
        start = 0
        mins = math.inf
        cnt = 0
        mid = (l + r) // 2

        for x in range(lr):
            if rocks[x] - start < mid:
                cnt += 1
            else:
                mins = min(mins, rocks[x] - start)
                start = rocks[x]

        if cnt > n:
            r = mid - 1
        else:
            answer = mins
            l = mid + 1

    return answer
