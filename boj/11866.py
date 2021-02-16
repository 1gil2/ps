#silver 4

N, M = map(int, input().split())
L = list(range(1, N+1))
K = []
temp = M-1
while True:
    le = len(L)
    if le == 1:
        break
    K.append(L.pop(temp))
    temp += M-1
    temp = temp % (le-1)
print("<", end='')
for k in K:
    print(k, ', ', end='', sep='')
print(L[0], ">", sep='')
