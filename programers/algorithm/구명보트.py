#level 2


def solution(people, limit):
    people.sort(reverse=True)
    l = 0
    r = len(people)-1
    answer = 0
    while l <= r:
        if people[l]+people[r] > limit:
            answer += 1
            l += 1
        else:
            answer += 1
            l += 1
            r -= 1
    return answer
