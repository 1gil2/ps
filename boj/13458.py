#bronze 2

n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0

for i in range(n):
    if A[i] < b:
        ans += 1
        continue
    else:
        ans += 1
        if (A[i]-b) % c == 0:
            ans += (A[i]-b)//c
        else:
            ans += (A[i]-b)//c+1

print(ans)
