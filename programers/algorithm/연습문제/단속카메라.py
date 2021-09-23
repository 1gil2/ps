#level 3


def solution(routes):
    answer = 1
    routes.sort()
    print(routes)
    lr = len(routes)
    left = routes[0][0]
    right = routes[0][1]
    for x in range(1, lr):
        if routes[x][0] > right:
            left = routes[x][0]
            right = routes[x][1]
            answer += 1
        else:
            if routes[x][1] > right:
                left = routes[x][0]
            else:
                left = routes[x][0]
                right = routes[x][1]

    return answer
