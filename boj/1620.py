#silver 4

import sys

n = sys.stdin.readline().split()
pok = []
pokes = list(range(int(n[0])))

for x in range(int(n[0])):
    pok.append(input())
D = dict(zip(pok, pokes))

for x in range(int(n[1])):
    b = sys.stdin.readline().strip()
    if b.isdigit():
        print(pok[int(b)-1])
    else:
        print(D[b]+1)
