#level 3


def dfs(visit, com, start, n):
    visit[start] = 1
    for x in range(n):
        if not visit[x] and com[start][x] == 1:
            dfs(visit, com, x, n)


def solution(n, computers):
    answer = 0
    visit = [0] * n

    for x in range(n):
        if not visit[x]:
            answer += 1
            dfs(visit, computers, x, n)

    return answer
