#gold 4

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = ['B' for x in range(n)]
a = 0
kk = 0
idx= -1

while kk < k:
    if idx < a:
        if answer[n-a-2] == 'A':
            break
        else:
            answer[n-a-2] = 'A'
            idx = n-a-2
            a += 1
            kk += 1
    else:
        answer[idx] = 'B'
        answer[idx-1] = 'A'
        idx -= 1
        kk += 1

if kk == k:
    print(''.join(answer))
else:
    print(-1)
