#level 1


def solution(arr):
    answer = [arr[0]]
    for n in arr:
        if n == answer[-1]:
            continue
        else:
            answer.append(n)
    return answer
