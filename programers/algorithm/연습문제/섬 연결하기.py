#level 3


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    for a, b, cost in costs:
        if parent[a] != parent[b]:
            temp = parent[b]
            for x in range(n):
                if parent[x] == temp:
                    parent[x] = parent[a]
            answer += cost

        check = 0
        for x in range(n - 1):
            if parent[x] != parent[x + 1]:
                check = 1
                break

        if check == 0:
            break

    return answer
