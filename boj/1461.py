#gold 5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

left = []
right = []

for book in books:
    if book < 0:
        left.append(book)
    else:
        right.append(book)

left.sort()
right.sort(reverse=True)

if left and right:
    ans = -max(abs(left[0]), right[0])
elif right:
    ans = -right[0]
else:
    ans = left[0]

lel = len(left)
for x in range(0, lel, m):
    ans += 2 * abs(left[x])

ler = len(right)
for x in range(0, ler, m):
    ans += 2 * abs(right[x])

print(ans)
