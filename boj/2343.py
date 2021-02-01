#silver 1

from sys import stdin
input = stdin.readline


def getCount(lst, size):
    count = 1
    s = 0
    for i in lst:
        if s + i > size:
            count += 1
            s = 0
        s += i
    return count


M = list(map(int, input().split()))[1]
lst = list(map(int, input().split()))

s, e = max(lst), sum(lst)

while s < e:
    m = (s + e) >> 1
    count = getCount(lst, m)

    if count > M:
        s = m + 1
    else:
        e = m

print(e)
