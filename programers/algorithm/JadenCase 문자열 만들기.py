#level 2


def solution(s):
    s = list(s.lower())
    if s[0].isalpha():
        s[0] = s[0].upper()
    for x in range(1, len(s)):
        if s[x - 1] == ' ' and s[x].isalpha():
            s[x] = s[x].upper()

    return ''.join(s)
