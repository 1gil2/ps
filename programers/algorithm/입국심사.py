#level 3


def solution(n, times):
    left = 1
    right = max(times) * n

    answer = 0

    while left <= right:
        mid = (right + left) // 2
        temp = n
        for x in times:
            temp -= mid // x
            if temp <= 0:
                answer = mid
                right = mid - 1
                break
        if temp > 0:
            left = mid + 1

    return answer
