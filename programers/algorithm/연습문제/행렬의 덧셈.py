#level 1


def solution(arr1, arr2):
    col = len(arr1)
    row = len(arr1[0])

    for x in range(col):
        for y in range(row):
            arr1[x][y] += arr2[x][y]

    return arr1
