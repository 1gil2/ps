#silver 3

n, k = map(int, input().split())
p = [0 for x in range(n)]

for x in range(n):
    p[x] = int(input())

cnt = 0
temp = 0
while True:
    cnt += 1
    temp = p[temp]
    if temp == k:
        print(cnt)
        break
    if cnt > n:
        print(-1)
        break
