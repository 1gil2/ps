#silver 4

import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

answer = 0

for x in range(n):
    answer += a[x] * b[x]

print(answer)
