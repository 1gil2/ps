#gold 4

import sys
input = sys.stdin.readline


def change(s):
     if s.islower():
        k = ord(s) - 97
     else:
        k = ord(s) - 65 + 26

     return k


g, s = map(int, input().split())
g -= 1

pw = input().rstrip()
st = input().rstrip()

check = [0 for x in range(52)]

for s in pw:
    k = change(s)
    check[k] += 1

temp = [0 for x in range(52)]
ans = 0
idx = 0

for i, x in enumerate(st):
    k = change(x)
    temp[k] += 1

    if i >= g:
        if temp == check:
            ans += 1

        k2 = change(st[idx])
        temp[k2] -= 1
        idx += 1

print(ans)
