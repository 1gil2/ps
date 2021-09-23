#level 2


def solution(board):
    col = len(board)
    row = len(board[0])

    answer = 0
    for x in range(col):
        if board[x][0] == 1:
            answer = 1

    for y in range(row):
        if board[0][y] == 1:
            answer = 1

    for x in range(1, col):
        for y in range(1, row):
            if board[x][y] == 1:
                if board[x - 1][y - 1] > 0 and board[x - 1][y] > 0 and board[x][y - 1] > 0:
                    board[x][y] = min(board[x - 1][y], board[x][y - 1], board[x - 1][y - 1]) + 1
                answer = max(answer, board[x][y])

    return answer * answer
