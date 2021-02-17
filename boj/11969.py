#silver 3

import sys

n, q = map(int, sys.stdin.readline().split())
cow = []
breed = [[0, 0, 0]]
for x in range(n):
    cow.append(int(sys.stdin.readline()))
for x in cow:
    breed.append(breed[-1][:])
    breed[-1][x - 1] += 1

for x in range(q):
    a, b = map(int, sys.stdin.readline().split())
    print(breed[b][0] - breed[a - 1][0], breed[b][1] - breed[a - 1][1], breed[b][2] - breed[a - 1][2])
