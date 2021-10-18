#level 4

from bisect import bisect_left, bisect_right


def solution(cookie):
    answer = 0

    psum = [0]
    le = len(cookie)

    for c in cookie:
        psum.append(c + psum[-1])

    for l in range(le - 1):
        for m in range(l + 1, le):
            pr = psum[m] * 2 - psum[l]
            right = bisect_right(psum, pr, m + 1, le + 1)
            left = bisect_left(psum, pr, m + 1, le + 1)
            if right > left:
                answer = max(answer, psum[left] - psum[m])

    return answer
