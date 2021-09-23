#level 1


def solution(answers):
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    la = len(answers)
    c1, c2, c3 = 0, 0, 0
    for x in range(la):
        if answers[x] == m1[x % 5]:
            c1 += 1
        if answers[x] == m2[x % 8]:
            c2 += 1
        if answers[x] == m3[x % 10]:
            c3 += 1

    M = max(c1, c2, c3)
    answer = []
    if M == c1:
        answer.append(1)
    if M == c2:
        answer.append(2)
    if M == c3:
        answer.append(3)

    return answer
