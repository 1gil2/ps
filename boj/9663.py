# gold 5
# pypy3


def solve(idx):
    global ans
    if idx == n:
        ans += 1
        return
    for x in range(n):
        if not (sero[x] or left_cross[idx + x] or right_cross[idx - x + n - 1]):
            sero[x] = True
            left_cross[idx + x] = True
            right_cross[idx - x + n - 1] = True
            solve(idx + 1)
            sero[x] = False
            left_cross[idx + x] = False
            right_cross[idx - x + n - 1] = False


n = int(input())
ans = 0

sero = [False] * n
left_cross = [False] * (2 * n - 1)
right_cross = [False] * (2 * n - 1)

solve(0)
print(ans)
