#level 2


def solution(n, a, b):
    answer = 0
    a -= 1
    b -= 1
    while True:
        if a == b:
            return answer
        a //= 2
        b //= 2
        answer += 1
