#level 3

import heapq


def solution(jobs):
    last, answer, now, count = -1, 0, 0, 0
    heap = []
    lj = len(jobs)

    while count < lj:
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(heap, job[1])
        if len(heap) > 0:
            answer += len(heap) * heap[0]
            last = now
            now += heapq.heappop(heap)
            count += 1
        else:
            now += 1

    return answer // lj
