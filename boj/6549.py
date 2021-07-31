#platinum 5

import sys

input = sys.stdin.readline


def histogram(start, end):
    if start == end:
        return 0
    if start + 1 == end:
        return height[start]

    mid = (start + end) // 2
    ret = max(histogram(start, mid), histogram(mid, end))

    width = 1
    h = height[mid]
    left = mid
    right = mid
    while right - left + 1 < end - start:
        if left > start:
            lh = min(h, height[left - 1])
        else:
            lh = -1

        if right < end - 1:
            rh = min(h, height[right + 1])
        else:
            rh = -1

        if lh > rh:
            h = lh
            left -= 1
        else:
            h = rh
            right += 1

        width += 1
        ret = max(ret, h * width)

    return ret

'''
def histogram():
    ret = 0
    stack = []

    for x in range(n):
        left = x

        while stack and stack[-1][0] >= height[x]:
            h, left = stack.pop()
            temp = h * (x - left)
            ret = max(ret, temp)

        stack.append((height[x], left))

    for h, idx in stack:
        ret = max(ret, (n-idx) * h)

    return ret

'''

while True:
    case = list(map(int, input().split()))
    n = case[0]
    height = case[1:]

    if n == 0:
        break

    print(histogram(0, n))
