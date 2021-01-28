#level 1


def solution(array, commands):
    answer = []
    for x in commands:
        new_array = array[x[0] - 1:x[1]]
        new_array.sort()
        answer.append(new_array[x[2] - 1])

    return answer
