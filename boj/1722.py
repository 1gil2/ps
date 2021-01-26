#silver 1

import sys
input = sys.stdin.readline

fac = [0, 1]
for x in range(2, 21):
    fac.append(fac[-1]*x)

n = int(input())
cmd = list(map(int, input().split()))
tag = cmd[0]
k = cmd[1:]
visit = [0 for x in range(n+1)]

if tag == 1:
    ans = ''
    for i in range(n):
        for j in range(1, n+1):
            if visit[j]:
                continue
            if k[0] > fac[n-i-1] and n-i > 1:
                k[0] -= fac[n-i-1]
            else:
                ans += str(j) + ' '
                visit[j] = 1
                break
    print(ans)
elif tag == 2:
    cnt = 0
    for i in range(n):
        for j in range(k[i]-1):
            if not visit[j+1]:
                cnt += fac[n-i-1]
        visit[k[i]] = 1
    print(cnt+1)
