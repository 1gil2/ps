#level 2


def solution(n):
    fibo = [0, 1]

    if n < 2:
        return fibo[n]
    else:
        for x in range(n):
            fibo.append(fibo[-1] + fibo[-2])
    return fibo[n] % 1234567
