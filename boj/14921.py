#gold 5

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ans = sys.maxsize

#합이 0에 가까워야 하니까 절대값 기준으로 정렬
A.sort(key=lambda x: abs(x))

for x in range(n-1):
    if abs(ans) > abs(A[x]+A[x+1]):
        ans = A[x]+A[x+1]

print(ans)
