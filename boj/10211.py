#silver 3

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    psum1 = 0
    psum2 = 0
    ans = -sys.maxsize

    for a in arr:
        psum1 += a
        ans = max(ans, psum1-psum2)
        psum2 = min(psum1, psum2)

    print(ans)
