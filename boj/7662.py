#gold 5
#pypy3

import bisect
from collections import deque

T = int(input())
for t in range(T):
    k = int(input())
    pq = deque()
    pqDict = dict()

    for x in range(k):
        cmd = input().split()
        val = int(cmd[1])

        if cmd[0] == 'I':
            try:
                pqDict[val] += 1
            except:
                pqDict[val] = 1
                bisect.insort_left(pq, val)
        else:
            if len(pq) == 0:
                continue
            if val == -1:
                if pqDict[pq[0]] == 1:
                    pqDict.pop(pq[0])
                    pq.popleft()
                else:
                    pqDict[pq[0]] -= 1
            else:
                if pqDict[pq[-1]] == 1:
                    pqDict.pop(pq[-1])
                    pq.pop()
                else:
                    pqDict[pq[-1]] -= 1

    if len(pq) == 0:
        print("EMPTY")
    else:
        print(pq[-1], pq[0])
