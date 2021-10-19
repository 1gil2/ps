#level 4

from heapq import heappush, heappop

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(land, height):
    n = len(land)
    visit = [[False for y in range(n)] for x in range(n)]
    heap = []
    heappush(heap, (0, 0, 0))

    answer = 0

    while heap:
        cost, x, y = heappop(heap)

        visit[x][y] = True
        answer += cost
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < n and not visit[x1][y1]:
                diff = abs(land[x][y] - land[x1][y1])
                if diff > height:
                    heappush(heap, (diff, x1, y1))
                else:
                    heappush(heap, (0, x1, y1))

    return answer
