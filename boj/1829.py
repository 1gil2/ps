#gold 1

import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())

a = n+k-1
m = 0

while a:
    a//=2
    m += 1

#2^0 ~ 2^m-1 까지 순차적으로 빼준다 -> 연속된 자연수기 때문에
D = defaultdict(int)
for i in range(m):
    temp = []
    cnt = 0
    for j in range(k, n+k):
        if j & (1 << i):
            cnt += 1
            temp.append(j-k+1)
    #선택한 항아리가 같다면 합쳐준다.
    temp2 = tuple(temp)
    if cnt != 0:
        D[temp2] += 1<<i

print(len(D))
for k, v in D.items():
    print(len(k), v)
    print(" ".join([str(x) for x in k]))
