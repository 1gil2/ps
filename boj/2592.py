#bronze 2

N = []
ave = 0
for x in range(10):
    a = int(input())
    ave += a
    N.append(a)
print(int(ave/10))

D = {}
for x in N:
    if x in D:
        D[x] += 1
    else:
        D[x] = 1
D1 = dict(zip(D.values(), D.keys()))
print(D1[max(D.values())])
