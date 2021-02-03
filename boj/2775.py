#bronze 2


def fac(a):
    ans = 1
    for i in range(1, a+1):
        ans *= i
    return ans


T = int(input())
for x in range(T):
    n = int(input())
    k = int(input())
    print(int(fac(k+n)/(fac(k-1)*fac(n+1))))
