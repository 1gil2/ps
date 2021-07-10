#silver 3

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    st = input().rstrip()
    left = []
    right = []

    for s in st:
        if s == '<':
            if left:
                right.append(left.pop())
        elif s == '>':
            if right:
                left.append(right.pop())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)

    ans = left[:]
    for r in right[::-1]:
        ans.append(r)

    print(''.join(ans))
