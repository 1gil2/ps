#level 2


def solution(dirs):
    S = set()
    x, y = 0, 0

    for di in dirs:
        if di == 'U':
            if y < 5:
                S.add((x, y, x, y + 1))
                S.add((x, y + 1, x, y))
                y += 1
        if di == 'D':
            if y > -5:
                S.add((x, y, x, y - 1))
                S.add((x, y - 1, x, y))
                y -= 1
        if di == 'L':
            if x > -5:
                S.add((x, y, x - 1, y))
                S.add((x - 1, y, x, y))
                x -= 1
        if di == 'R':
            if x < 5:
                S.add((x, y, x + 1, y))
                S.add((x + 1, y, x, y))
                x += 1

    return len(S) // 2
