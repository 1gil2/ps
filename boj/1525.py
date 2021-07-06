#gold 2

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def go(st):
    dq = deque()
    dq.append(st)
    visit = dict()
    visit[st] = 0

    while dq:
        s = dq.popleft()
        cnt = visit[s]
        idx = s.index('0')

        if s == '123456780':
            return print(cnt)

        x = idx // 3
        y = idx % 3

        for i in range(4):
            new_st = list(s)
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < 3 and 0 <= y1 < 3:
                temp = x1 * 3 + y1
                new_st[idx], new_st[temp] = new_st[temp], new_st[idx]

                nxt = "".join(new_st)

                if not visit.get(nxt):
                    visit[nxt] = visit[s] + 1
                    dq.append(nxt)

    return print(-1)


st = ''
for x in range(3):
    a, b, c = map(str, input().rstrip().split())
    st += a
    st += b
    st += c

go(st)
