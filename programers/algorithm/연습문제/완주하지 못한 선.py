#level 1


def solution(participant, completion):
    participant.sort()
    completion.sort()

    lp = len(participant)

    for x in range(lp - 1):
        if participant[x] != completion[x]:
            return participant[x]

    return participant[-1]
