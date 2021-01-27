#level 2

from collections import deque


def solution(priorities, location):
    answer = 0
    lp = len(priorities)
    temp = []
    for x in range(lp):
        temp.append((priorities[x], x))

    dq = deque(temp)

    while len(dq):
        item = dq.popleft()
        if dq and max(dq)[0] > item[0]:
            dq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer
