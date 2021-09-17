#level 2


def solution(s):
    stack = []
    for x in s:
        if stack:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)

    if stack:
        return 0
    return 1
