#level 3

from heapq import heappush, heappop


def solution(n, works):
    if sum(works) < n:
        return 0

    heap = []
    for x in works:
        heappush(heap, -x)

    while n:
        heappush(heap, heappop(heap) + 1)
        n -= 1

    answer = 0
    for x in heap:
        answer += x * x

    return answer
