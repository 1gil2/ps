#silver 4

n, m = map(int, input().split())

D = dict()
L = []

for x in range(n):
    man = input()
    try:
        D[man]
    except:
        D[man] = 1

for x in range(m):
    man = input()
    try:
        if D[man]:
            L.append(man)
    except:
        continue

L.sort()

print(len(L))
for x in L:
    print(x)
