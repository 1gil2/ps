#gold 1

import sys

input = sys.stdin.readline
inf = sys.maxsize


def init():
    for x in range(n):
        m_tree[x + size] = arr[x]
    for x in range(n, size):
        m_tree[x + size] = inf
    for x in range(size - 1, 0, -1):
        m_tree[x] = min(m_tree[2 * x], m_tree[2 * x + 1])


def m_query(left, right):
    left += size
    right += size
    ret = inf

    while left <= right:
        if left % 2 == 1:
            ret = min(ret, m_tree[left])
            left += 1
        if right % 2 == 0:
            ret = min(ret, m_tree[right])
            right -= 1
        left >>= 1
        right >>= 1

    return ret


n, m = map(int, input().split())

h = n.bit_length()
size = 1 << h

arr = []
m_tree = [0 for x in range(size * 2)]

for _ in range(n):
    arr.append(int(input()))

init()

for _ in range(m):
    a, b = map(int, input().split())
    print(m_query(a - 1, b - 1))
