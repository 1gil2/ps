# silver 1

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = [x for x in range(1, n + 1)]
    ans = [0 for x in range(n)]
    flag = True

    for x in range(n - 1, -1, -1):
        t = arr[x]

        if t >= len(temp):
            flag = False
            print("IMPOSSIBLE")
            break
        ans[x] = temp[t]
        temp.pop(t)

    if flag:
        for x in range(n):
            print(ans[x], end=' ')
        print()
