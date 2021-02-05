#gold 1

import sys
input = sys.stdin.readline

prime = [False, False] + [True] * 32000
p = []

for x in range(2, 32001):
    if prime[x]:
        p.append(x)
        for y in range(2*x, 32001, x):
            if prime[y]:
                prime[y] = False

ps = len(p)
while True:
    flag = True
    ans = 1
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        for x in range(ps+1):
            if n == 1:
                break
            if x == ps:
                flag = False
                print(ans*(n-1))
                break
            cnt = 0
            if n % p[x] == 0:
                while n % p[x] == 0:
                    cnt += 1
                    n //= p[x]
                ans *= int(p[x]**cnt - p[x]**(cnt-1))
        if flag:
            print(ans)
