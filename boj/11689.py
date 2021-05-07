#platinum 5

n = int(input())

ans = n

for i in range(2, int(n**0.5)+1):
    if n%i == 0:
        while n%i == 0:
            n//= i

        ans *= i-1
        ans //= i

if n > 1:
    ans *= n-1
    ans //= n

print(ans)
