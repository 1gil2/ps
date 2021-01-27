#silver 3

import sys

flag = True
cnt = 1
p = []
s = []
for x in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    while cnt <= n:
        s.append(cnt)
        p.append('+')
        cnt += 1
    if s[-1] == n:
        s.pop()
        p.append('-')
    else:
        flag = False
        
if flag:
    for x in p:
        print(x)
else:
    print("NO")
