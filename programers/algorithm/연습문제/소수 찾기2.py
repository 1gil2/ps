#level 1


def solution(n):
    answer = 0

    prime = [False, False] + [True] * (n - 1)
    for x in range(2, n + 1):
        if prime[x] == True:
            answer += 1
            for y in range(2 * x, n + 1, x):
                if prime[y] == True:
                    prime[y] = False

    return answer
