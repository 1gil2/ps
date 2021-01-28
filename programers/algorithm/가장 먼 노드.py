#level 3


from collections import deque


def solution(n, edge):
    def bfs():
        dq = deque()
        dq.append(1)

        while dq:
            x = dq.popleft()

            for i in table[x]:
                if visit[i] == -1:
                    visit[i] = visit[x] + 1
                    dq.append(i)

    table = [[] for i in range(n + 1)]
    visit = [-1] * (n + 1)

    for x, y in edge:
        table[x].append(y)
        table[y].append(x)

    visit[1] = 0
    bfs()
    return visit.count(max(visit))
