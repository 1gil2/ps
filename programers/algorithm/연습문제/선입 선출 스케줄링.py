#level 4


def solution(n, cores):
    lc = len(cores)
    if n <= lc:
        return n

    left = 0
    right = 50000 * 10000
    n -= lc

    while left < right:
        mid = (left + right) // 2

        work = 0

        for core in cores:
            work += mid // core

        if work >= n:
            right = mid
        else:
            left = mid + 1

    for core in cores:
        n -= (right - 1) // core

    for i in range(lc):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1
