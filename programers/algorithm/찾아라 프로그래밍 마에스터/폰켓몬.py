#level 1


def solution(nums):
    ln = len(nums)
    D = dict()
    for num in nums:
        try:
            D[num] += 1
        except:
            D[num] = 1

    ln = len(nums)
    ld = len(D)

    if ln // 2 > ld:
        return ld
    else:
        return ln // 2
