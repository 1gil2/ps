#silver 3

import sys
from collections import deque
input = sys.stdin.readline

for x in range(int(input())):
    m, n = map(int, input().split())
    A = deque((map(int, input().split())))
    B = deque((range(m)))
    cnt = 0
    while True:
        b = B.popleft()
        if max(A) == A[0]:
            A.popleft()
            cnt += 1
            if b == n:
                print(cnt)
                break
        else:
            A.append(A.popleft())
            B.append(b)
