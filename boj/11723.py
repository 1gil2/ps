#silver 5

import sys

s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
al = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
em = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(int(sys.stdin.readline())):
    A = sys.stdin.readline().split()
    if A[0] == 'add':
        s[int(A[1])-1] = 1
    elif A[0] == 'remove':
        s[int(A[1])-1] = 0
    elif A[0] == 'check':
        print(s[int(A[1])-1])
    elif A[0] == 'toggle':
        s[int(A[1])-1] = (s[int(A[1])-1]+1) % 2
    elif A[0] == 'all':
        s = al[:]
    else:
        s = em[:]
