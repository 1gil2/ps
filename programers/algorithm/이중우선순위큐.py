#level 3

import bisect
from collections import deque


def solution(operations):
    answer = deque()

    for cmd in operations:
        A, B = cmd.split()
        if A == 'I':
            bisect.insort(answer, int(B))
        elif answer:
            if int(B) == 1:
                answer.pop()
            else:
                answer.popleft()

    if answer:
        return [answer[-1], answer[0]]
    return [0, 0]
