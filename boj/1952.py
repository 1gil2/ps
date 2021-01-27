#bronze 3


def snail(a, b):
    if a == 1:
        return 0
    elif b == 1:
        return 1
    elif a == 2:
        return 2
    elif b == 2:
        return 3
    else:
        return 4+snail(a-2, b-2)


m, n = map(int, input().split())
print(snail(m, n))
