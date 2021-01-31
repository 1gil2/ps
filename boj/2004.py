#silver 2


def two(n):
    if n == 0:
        return 0
    return n // 2 + two(n // 2)


def five(n):
    if n == 0:
        return 0
    return n // 5 + five(n // 5)


n, m = map(int, input().split())

print(min(two(n) - two(m) - two(n - m), five(n) - five(m) - five(n - m)))
