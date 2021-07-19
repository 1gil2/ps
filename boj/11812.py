#gold 3

import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())

    ans = 0

    if k == 1:
        print(abs(x-y))
        continue

    while x != y:
        if x > y:
            x = (x-2)//k + 1
        else:
            y = (y-2)//k + 1

        ans += 1

    print(ans)
