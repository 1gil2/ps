#silver 3

import sys

s = sys.stdin.readline()
cnt = 0
total = 0
for x in range(len(s)-1):
    if s[x] == '(':
        if s[x+1] == '(':
            cnt += 1
    else:
        if s[x-1] == '(':
            total += cnt
        else:
            total += 1
            cnt -= 1

print(total)
