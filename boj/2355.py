#bronze 3

a, b = map(int, input().split())
if b > a:
    a, b = b, a
print((a+b)*(a-b+1)//2)
