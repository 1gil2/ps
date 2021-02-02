#bronze 3

import sys
input = sys.stdin.readline

train = []
for x in range(4):
    train.append(list(map(int, input().split())))

a1 = train[0][1]
a2 = a1-train[1][0]+train[1][1]
a3 = a2-train[2][0]+train[2][1]
a4 = a3-train[3][0]

A = [a1, a2, a3, a4]
print(max(A))
