#level 2

from collections import deque


def solution(progresses, speeds):
    end = []
    lp = len(progresses)
    for x in range(lp):
        a1 = 100 - progresses[x]
        if a1 % speeds[x] == 0:
            end.append(a1 // speeds[x])
        else:
            end.append(a1 // speeds[x] + 1)

    dq = deque(end)
    answer = []

    while dq:
        a2 = dq.popleft()
        cnt = 1
        while dq:
            if dq[0] <= a2:
                cnt += 1
                dq.popleft()
            else:
                break
        answer.append(cnt)

    return answer
