#silver 2

n = int(input())
a = list(map(int, input().split()))
d = []
for x in a:
    d.append(1)
for x in range(1, n):
    for y in range(x):
        if a[x] > a[y]:
            d[x] = max(d[x], d[y]+1)
print(max(d))
