#gold 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
fact = set(list(map(int, input().split()))[1:])

parties = []
ans = [1 for x in range(m)]

for x in range(m):
    parties.append(set(list(map(int, input().split()))[1:]))

for x in range(m):
    for i, party in enumerate(parties):
        if ans[i] == 1 and party&fact:
            ans[i] = 0
            fact |= party

print(sum(ans))
