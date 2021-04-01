#silver 1

n, m = map(int, input().split())
h = list(map(int, input().split()))

happy = sum(h)+n
ans = 0
if happy >= m:
    print(0)
else:
    temp = m-happy
    a = 1
    while temp > 0:
        x = a*a*(n+1)
        if temp > n+1:
            temp -= n+1
            ans += a*a*(n+1)
            a+=1
        else:
            ans += temp*a*a
            break
    print(ans)
