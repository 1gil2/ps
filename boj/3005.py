#silver 1

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
table = [list(input().rstrip()) for x in range(r)]

words = []

#가로
for x in range(r):
    st = ''
    cnt = 0
    for y in range(c):
        if table[x][y] == '#':
            if cnt > 1:
                words.append(st)
            st = ''
            cnt = 0
        else:
            st += table[x][y]
            cnt += 1
    if cnt > 1:
        words.append(st)

#세로
for y in range(c):
    st = ''
    cnt = 0
    for x in range(r):
        if table[x][y] == '#':
            if cnt > 1:
                words.append(st)
            st = ''
            cnt = 0
        else:
            st += table[x][y]
            cnt += 1
    if cnt > 1:
        words.append(st)

words.sort()

print(words[0])
