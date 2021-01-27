#silver 2

n = int(input())
Meet = []

for x in range(n):
    Meet.append(list(map(int, input().split())))

Meet.sort(key=lambda x: (x[1], x[0]))

ans = 0
endTime = 0
for x in range(n):
    if endTime <= Meet[x][0]:
        endTime = Meet[x][1]
        ans += 1

print(ans)
