#gold 3
#pypy3

import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
h.sort()

ans = sys.maxsize

for x in range(n):
    for y in range(x+1, n):
        snowman1 = h[x] + h[y]

        left = x+1
        right = n-1

        while True:
            while left == x or left == y:
                left += 1
            while right == x or right == y:
                right -= 1

            if left >= right:
                break

            snowman2 = h[left] + h[right]

            if snowman1 < snowman2:
                ans = min(ans, snowman2 - snowman1)
                right -= 1
            elif snowman1 >= snowman2:
                ans = min(ans, snowman1 - snowman2)
                left += 1

print(ans)
