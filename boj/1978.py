#silver 4


def prime(n):
    n = int(n)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a = 2
    while a < n:
        if n%a == 0:
            return 0
        else:
            a += 1
    return 1


N = input()
A = list(input().split())
ans = 0
for x in A:
    ans += prime(x)
print(ans)
