#level 4


def solution(arr):
    mM = [0, 0]
    tot = 0

    le = len(arr)
    for i in range(le - 1, -1, -1):
        print(mM, tot)
        if arr[i] == '+':
            continue
        elif arr[i] == '-':
            m, M = mM
            mM[0] = min(-(tot + M), -tot + m)
            temp = int(arr[i + 1])
            mM[1] = max(-(tot + m), -temp + (tot - temp) + M)
            tot = 0
        else:
            tot += int(arr[i])

    print(mM, tot)
    mM[1] += tot
    return mM[1]
