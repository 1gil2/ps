#bronze 3

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    s = a+b+c
    m = max(a, b, c)
    n = min(a, b, c)
    k = s-m-n
    if m*m == n*n + k*k:
        print('right')
    else:
        print('wrong')
