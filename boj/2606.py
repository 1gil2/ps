#silver 3

n = int(input())

visit = [0 for x in range(n+1)]

com = [[0 for x in range(n+1)] for y in range(n+1)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    com[a][b] = 1
    com[b][a] = 1

visit[1] = 1

Q = [1]

while len(Q) != 0:
    k = Q.pop(0)

    for x in range(1, n+1):
        if com[k][x] == 1 and visit[x] == 0:
            visit[x] = 1
            Q.append(x)

print(sum(visit)-1)
