#level 3


from collections import deque


def solution(begin, target, words):
    def check(a, b):
        cnt = 0
        la = len(a)
        for x in range(la):
            if a[x] != b[x]:
                cnt += 1
        if cnt == 1:
            return True
        return False

    D = dict()
    D[begin] = 0
    for x in words:
        D[x] = 0

    dq = deque()
    dq.append(begin)

    while dq:
        x = dq.popleft()
        if x == target:
            return D[target]

        for i in words:
            if check(x, i) and D[i] == 0:
                D[i] = D[x] + 1
                dq.append(i)

    return 0
