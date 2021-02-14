#silver 4

import sys
from collections import deque

dq = deque()
for x in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        dq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        dq.append(cmd[1])
    elif cmd[0] == "pop_front":
        try:
            print(dq.popleft())
        except:
            print(-1)
    elif cmd[0] == "pop_back":
        try:
            print(dq.pop())
        except:
            print(-1)
    elif cmd[0] == "size":
        print(len(dq))
    elif cmd[0] == "empty":
        if len(dq):
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if len(dq):
            print(dq[-1])
        else:
            print(-1)
