#bronze 1

n, b = map(int, input().split())

L = []

while True:
    if n == 0:
        break
    L.append(n % b)
    n = n//b

le = len(L)

for x in range(le):
    if L[x] >= 10:
        L[x] = chr(L[x]+55)

print(''.join(map(str, L[::-1])))
