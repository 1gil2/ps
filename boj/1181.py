#silver 5

import sys
n = int(sys.stdin.readline())
S = set()
for x in range(n):
    a = sys.stdin.readline().strip()
    S.add(a)
S1 = list(S)
S1.sort()
S1.sort(key=lambda x : len(x))
print('\n'.join(S1))
