#silver 4

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

temp = sorted(arr)

ans = []

for x in range(n):
    idx = temp.index(arr[x])

    ans.append(idx)

    temp[idx] = -1

print(*ans)
