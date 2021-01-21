#silver 5

N = input()
D = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
for x in N:
    if x == '9':
        D['6'] += 1
    else:
        D[x] += 1
if D['6']%2 == 0:
    D['6'] /= 2
else:
    D['6'] /= 2
    D['6'] += 1
A = set()
for x in D:
    A.add(D[x])
print(int(max(A)))
