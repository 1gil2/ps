#level 1

import math


def solution(n):
    m = int(math.sqrt(n))

    if m * m == n:
        return (m + 1) ** 2
    else:
        return -1
