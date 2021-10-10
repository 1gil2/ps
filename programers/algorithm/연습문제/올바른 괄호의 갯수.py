#level 4

import math


def solution(n):
    return math.factorial(2*n) // (math.factorial(n)*math.factorial(n+1))
