#level 2


def solution(n):
    cnt = 0
    while n:
        while n % 2 == 0:
            n //= 2

        cnt += 1
        n -= 1

    return cnt
