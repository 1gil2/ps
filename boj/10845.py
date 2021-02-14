#silver 4

import sys

n = int(sys.stdin.readline())
Q = []
for x in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        Q.append(a[1])
    elif a[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
            Q.pop(0)
    elif a[0] == 'size':
        print(len(Q))
    elif a[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif a[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[len(Q)-1])
