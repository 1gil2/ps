#level 3


def solution(n):
    def dfs(col):
        global answer
        if col == n:
            answer += 1
            return

        for x in range(n):
            if row[x] == 0 and left_cross[x + col] == 0 and right_cross[n - x + col - 1] == 0:
                row[x] = 1
                left_cross[x + col] = 1
                right_cross[n - x + col - 1] = 1
                dfs(col + 1)
                row[x] = 0
                left_cross[x + col] = 0
                right_cross[n - x + col - 1] = 0

    row = [0 for x in range(n)]
    left_cross = [0 for x in range(2 * n - 1)]
    right_cross = [0 for x in range(2 * n - 1)]

    global answer
    answer = 0
    dfs(0)
    return answer
