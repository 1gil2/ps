#level 2

import math


def solution(arr):
    temp = 1
    for x in arr:
        g = math.gcd(temp, x)
        temp = temp * x // g

    return temp

