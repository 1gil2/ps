#silver 4
#pypy3

import sys
from collections import deque

n = int(input())
dq = deque()
cnt = 0

for x in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))

    if cmd[0] == "push":
        dq.append(int(cmd[1]))
        cnt += 1
    elif cmd[0] == "pop":
        if cnt == 0:
            print(-1)
        else:
            print(dq.popleft())
            cnt -= 1
    elif cmd[0] == "size":
        print(cnt)
    elif cmd[0] == "empty":
        if cnt == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if cnt == 0:
            print(-1)
        else:
            print(dq[0])
    elif cmd[0] == "back":
        if cnt == 0:
            print(-1)
        else:
            print(dq[len(dq)-1])
