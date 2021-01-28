#level 2

import itertools


def prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def solution(numbers):
    num = set()
    for i in range(len(numbers), 0, -1):
        for x in list(map("".join, itertools.permutations(numbers, i))):
            if prime(int(x)) is True:
                num.add(int(x))

    return len(num)
