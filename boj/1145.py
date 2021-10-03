#bronze 1

import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
m = min(a)

while True:
    cnt = 0
    for i in range(5):
        if m % a[i] == 0:
            cnt += 1
    if cnt > 2:
        print(m)
        break
    m += 1
