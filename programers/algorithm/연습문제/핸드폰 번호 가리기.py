#level 1


def solution(phone_number):
    pl = len(phone_number)

    return '*' * (pl - 4) + phone_number[-4:]
