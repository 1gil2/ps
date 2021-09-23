#level 3


def solution(n):
    def move(n, a, c, b):  # n칸을 a에서 c로 옮기기
        if n == 1:
            answer.append([a, c])
        else:
            move(n - 1, a, b, c)
            answer.append([a, c])
            move(n - 1, b, c, a)

    answer = []
    move(n, 1, 3, 2)
    return answer
