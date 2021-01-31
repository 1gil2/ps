#silver 1

n, c = map(int, input().split())

home = []

for x in range(n):
    home.append(int(input()))

ans = 0
home.sort()

left = 1
right = home[-1] - home[0]

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    cur = home[0]
    for x in range(1, n):
        if mid <= home[x] - cur:
            cnt += 1
            cur = home[x]

    if cnt < c:
        right = mid - 1
    elif cnt >= c:
        ans = mid
        left = mid + 1

print(ans)
