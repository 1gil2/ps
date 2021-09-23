#level 1


def solution(s, n):
    Up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Lo = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

    answer = ''
    for x in s:
        if x == ' ':
            answer += x
        else:
            if ord(x) < 97:
                answer += Up[ord(x) - 65 + n]
            else:
                answer += Lo[ord(x) - 97 + n]

    return answer
