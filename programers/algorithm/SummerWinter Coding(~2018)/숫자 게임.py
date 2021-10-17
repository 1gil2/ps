#level 3

from collections import deque


def solution(A, B):
    answer = 0
    lb = len(B)
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)

    for i in range(lb):
        if B[-1] > A[-1]:
            answer += 1
            B.pop()
        A.pop()

    return answer
