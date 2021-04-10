#level 2


def solution(n):
    answer = 0
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            if 2 * n == (x + y) * (y - x + 1):
                answer += 1
            elif 2 * n < (x + y) * (y - x + 1):
                break

    return answer
