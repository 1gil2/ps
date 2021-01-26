#silver 5

n, m = map(int, input().split())

ans = 1
if n >= 3:
    if m >= 7:
        ans = m-2
    elif m >= 4:
        ans = 4
    else:
        ans = m
elif n == 2:
    if m >= 7:
        ans = 4
    else:
        ans = (m + 1)//2

print(ans)
