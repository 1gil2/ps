#gold 3

n = int(input())
a = [False, False]+[True]*(n-1)
prime = []
for x in range(2, n+1):
    if a[x]:
        prime.append(x)
        for y in range(2*x, n+1, x):
            a[y] = False

l = len(prime)

ans = 0
cnt = 0
left = 0

for x in range(l):
    ans += prime[x]
    while True:
        if ans == n:
            cnt += 1
            break
        elif ans > n:
            ans -= prime[left]
            left += 1
        else:
            break
print(cnt)
