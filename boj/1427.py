#silver 5

N = input()

L = []

l = len(N)

for x in range(l):
    L.append(int(N[x]))

L.sort(reverse=True)

for x in range(l):
    print(L[x], end='')
