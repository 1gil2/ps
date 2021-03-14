#level 1


def solution(s):
    S = s.split(" ")
    T = []
    for x in S:
        temp = ''
        ls = len(x)
        for y in range(ls):
            if y % 2 == 0:
                temp += x[y].upper()
            else:
                temp += x[y].lower()
        T.append(temp)

    return ' '.join(T)
