#silver 1

import sys
input = sys.stdin.readline

prime = [False, False] + [True]*999999
for x in range(2, 1000001):
    if prime[x]:
        for y in range(2*x, 1000001, x):
            if prime[y]:
                prime[y] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        flag = False
        for x in range(3, n//2+1, 2):
            if prime[x] and prime[n-x]:
                print(n, '=', x, '+', n-x)
                flag = True
                break
        if flag == False:
            print("Goldbach's conjecture is wrong.")
