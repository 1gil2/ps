#level 3


def solution(N, number):
    numset = [0, [N]]
    if N == number:
        return 1
    for x in range(2, 9):
        temp = []
        repeat = int(str(N)*x)
        temp.append(repeat)
        for x_half in range(1, x//2+1):
            for i in numset[x_half]:
                for j in numset[x-x_half]:
                    temp.append(i+j)
                    temp.append(i-j)
                    temp.append(-i+j)
                    temp.append(i*j)
                    if j != 0:
                        temp.append(i/j)
                    if i != 0:
                        temp.append(j/i)
            if number in temp:
                return x
            numset.append(temp)
    return -1
