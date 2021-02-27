#silver 1

from collections import deque

a, b = map(int, input().split())

Q = deque()
Q.append([a, 1])

ans = -1

while Q:
    temp = Q.popleft()
    num = temp[0]
    cnt = temp[1]

    if num*2 == b:
        ans = cnt+1
        break
    if num*2 < b:
        Q.append([num*2, cnt+1])

    x = int(str(num)+'1')
    if x == b:
        ans = cnt+1
        break
    if x < b:
        Q.append([x, cnt+1])

print(ans)
