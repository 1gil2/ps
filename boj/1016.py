#gold 1

import sys
input = sys.stdin.readline

m, M = map(int, input().split())

table = [False] * (M-m+2)

cut = 2
answer = M-m+1

while cut*cut <= M:
    temp = cut*cut
    base = m // temp
    if m % temp != 0:
        base += 1

    while base*temp <= M:
        if not table[base*temp - m]:
            table[base*temp - m] = True
            answer -= 1
        base += 1

    cut += 1

print(answer)
