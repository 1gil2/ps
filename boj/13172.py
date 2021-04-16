#silver 1

MOD = 1000000007


def my_pow(base, p):
    res = 1
    cur = base % MOD
    while p > 0:
        res = (cur * res) % MOD if (p & 1) else res
        cur = (cur * cur) % MOD
        p //= 2
    return res


M = int(input())
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    ans = (ans + b * my_pow(a, MOD-2)) % MOD
print(ans)
