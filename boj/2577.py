#bronze 2

A = int(input())
B = int(input())
C = int(input())
D = list(str(A*B*C))
N = dict(zip(range(0, 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
for x in D:
    N[int(x)] += 1
for y in N.values():
    print(y)
