#level 3

import math


def solution(n, stations, w):
    answer = 0

    ww = 2 * w + 1
    idx = 1

    for s in stations:
        length = s - w - idx
        if length > 0:
            answer += math.ceil(length / ww)
        idx = s + w + 1

    if n >= idx:
        answer += math.ceil((n - idx + 1) / ww)

    return answer
