#platinum 5

import sys

input = sys.stdin.readline


def btn2(a, b, c, d):
    ret = -1
    cnt = 0
    while a <= c and b <= d:
        if b - a == d - c:
            ret = cnt

        a *= 2
        b *= 2
        cnt += 1

    return ret


a, b, c, d = map(int, input().split())
blue = btn2(a, b, c, d)

if c < a or d < b or blue == -1:
    print(-1)
    sys.exit()

ans = blue
temp1 = c - (a << blue)
temp2 = d - (b << blue)
if temp1 < 0 or temp2 < 0:
    print(-1)
    sys.exit()

for x in range(blue, -1, -1):
    ans += temp1 // (1 << x)
    temp1 %= (1 << x)

print(ans)
