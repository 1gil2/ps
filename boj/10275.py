#bronze 2


def gold(n, a, b):
    for x in range(1, n+1):
        if a & (1<<x):
            if b & (1<<x):
                return x
    return 0


t = int(input())
for x in range(t):
    n, a, b = map(int, input().split())
    print(n-gold(n, a, b))
