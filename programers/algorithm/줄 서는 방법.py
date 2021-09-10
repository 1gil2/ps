#level 3


def solution(n, k):
    f = [1, 1]
    for x in range(2, n + 1):
        f.append(f[-1] * x)

    answer = []
    num = list(range(1, n + 1))

    while n != 0:
        answer.append(num.pop((k - 1) // f[n - 1]))
        k %= f[n - 1]
        n -= 1

    return answer
