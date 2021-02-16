#silver 5

n = int(input())

L = []

for z in range(n):
    x, y = map(int, input().split())
    L.append([y, x])

L.sort()

for x in range(n):
    print(L[x][1], L[x][0])
