#level 3


def solution(tickets):
    routes = dict()
    for x in tickets:
        routes[x[0]] = routes.get(x[0], []) + [x[1]]
    for x in routes:
        routes[x].sort(reverse=True)

    start = ['ICN']
    path = []

    while start:
        top = start[-1]
        if top in routes and routes[top]:
            start.append(routes[top].pop())
        else:
            path.append(start.pop())

    return path[::-1]
