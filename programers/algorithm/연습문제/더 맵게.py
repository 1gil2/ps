#level 2

import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for x in scoville:
        heapq.heappush(heap, x)

    while heap[0] < K:
        a1 = heapq.heappop(heap)
        a2 = heapq.heappop(heap)
        heapq.heappush(heap, a1 + a2 + a2)
        answer += 1

        if len(heap) == 1 and heap[0] < K:
            return -1

    return answer
