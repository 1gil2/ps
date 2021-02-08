#bronze 1

A = set(range(1, 10001))
B = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    B.add(i)

A = sorted(A-B)
for i in A:
    print(i)
