#gold 5

from collections import deque
import sys
input=sys.stdin.readline


def bfs(n):
    dq = deque()
    dq.append(n)
    check[n][0] = 0
    check[n][1] = 1

    while dq:
        x = dq.popleft()

        for i in (x+1, x-1, x*2):
            if 0 <= i < 100001:
                if check[i][0] == -1:
                    check[i][0] = check[x][0]+1
                    check[i][1] = check[x][1]
                    dq.append(i)

                elif check[i][0] == check[x][0]+1:
                    check[i][1] += check[x][1]


n, k = map(int, input().split())
check = [[-1, 0] for x in range(100001)]

bfs(n)
print(check[k][0])
print(check[k][1])
