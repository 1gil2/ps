#gold 5

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    max_heap = []
    min_heap = []
    visit = [False] * 1000001

    n = int(input())

    for key in range(n):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heappush(min_heap, (num, key))
            heappush(max_heap, (-1 * num, key))
            visit[key] = True

        elif cmd == 'D':
            if num == -1:
                while min_heap and not visit[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heappop(min_heap)
            elif num == 1:
                while max_heap and not visit[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heappop(max_heap)

    if min_heap and max_heap:
        print(-1 * max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
