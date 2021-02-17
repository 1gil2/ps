# silver 4

n = int(input())
p = 2
r = int(n ** 0.5) + 1

while p <= r:
    while n % p == 0:
        print(p)
        n //= p
    p += 1

if n > 1:
    print(n)