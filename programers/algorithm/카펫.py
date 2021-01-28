#level 2


def solution(brown, yellow):
    total = brown + yellow

    for x in range(1, yellow + 1):
        if yellow // x == yellow / float(x):
            if total == (x + 2) * (yellow // x + 2):
                return [yellow // x + 2, x + 2]
