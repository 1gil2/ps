#level 2


def solution(citations):
    citations.sort()
    lc = len(citations)
    for x in range(lc):
        if citations[x] >= lc-x:
            return lc-x
    return 0
