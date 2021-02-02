#silver 1

n = int(input())
ab = []

for x in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

ab.sort()

lis = [[] for x in range(n)]
for x in range(n):
    if x == 0:
        lis[x].append(ab[x][1])
    else:
        for y in range(x):
            if lis[y][-1] < ab[x][1]:
                if len(lis[x]) - 1 < len(lis[y]):
                    lis[x] = lis[y] + [ab[x][1]]
        if not lis[x]:
            lis[x].append(ab[x][1])

M = 0
for x in range(n):
    M = max(M, len(lis[x]))

print(n - M)
