#bronze 2

N = [-1 for _ in range(26)]
S = input()
cnt = 0
for x in S:
    if N[ord(x)-97] == -1:
        N[ord(x)-97] = cnt
    cnt += 1

for x in N:
    print(x, end=' ')
