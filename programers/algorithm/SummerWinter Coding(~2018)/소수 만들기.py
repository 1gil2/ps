#level 1

from itertools import combinations


def solution(nums):
    answer = 0

    prime = [False, False] + [True] * 3000
    for x in range(2, 3001):
        if prime[x]:
            for y in range(2 * x, 3001, x):
                if prime[y]:
                    prime[y] = False

    combi = list(combinations(nums, 3))

    for com in combi:
        if prime[sum(com)]:
            answer += 1

    return answer
