#level 2


def change(n):
    cnt = 0
    while n:
        cnt += n % 2
        n //= 2
    return cnt


def solution(n):
    temp = change(n)
    while True:
        n += 1
        if change(n) == temp:
            return n
