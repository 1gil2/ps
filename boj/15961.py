#gold 4

import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = list(map(int, input().split()))

sushi = []
for x in range(n):
    sushi.append(int(input()))

check = [0 for x in range(d+1)]

table = deque()

temp = 0
for x in range(k):
    if check[sushi[x]] == 0:
        temp += 1
    table.append(sushi[x])
    check[sushi[x]] += 1

if check[c] == 0:
    ans = temp + 1
else:
    ans = temp

for x in range(1, n):
    idx = (x+k-1)%n

    remove = table.popleft()
    check[remove] -= 1
    if check[remove] == 0:
        temp -= 1

    if check[sushi[idx]] == 0:
        temp += 1

    check[sushi[idx]] += 1
    table.append(sushi[idx])
    if check[c] == 0:
        ans = max(ans, temp+1)
    else:
        ans = max(ans, temp)

print(ans)
